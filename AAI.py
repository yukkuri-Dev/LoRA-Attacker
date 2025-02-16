import argparse
import cv2
import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift, ifftshift
from perlin_noise import PerlinNoise

def remove_iccp(input_path, output_path):
    """ libpng warning の回避（カラープロファイルを削除） """
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print("画像の読み込みに失敗しました。")
        return None
    cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    return output_path

def add_gaussian_noise_luminance(image, level):
    """ ガウシアンノイズを輝度チャンネル(L)のみに適用 """
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    noise = np.random.normal(0, level, l.shape).astype(np.int16)
    l_noisy = np.clip(l.astype(np.int16) + noise, 0, 255).astype(np.uint8)

    lab_noisy = cv2.merge([l_noisy, a, b])
    return cv2.cvtColor(lab_noisy, cv2.COLOR_LAB2BGR)

def add_perlin_noise_luminance(image, level):
    """ Perlinノイズを輝度チャンネル(L)のみに適用 """
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    rows, cols = l.shape
    perlin = PerlinNoise(octaves=6)
    perlin_noise = np.array([[perlin([i/rows, j/cols]) for j in range(cols)] for i in range(rows)])
    perlin_noise = cv2.normalize(perlin_noise, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    l_noisy = cv2.addWeighted(l, 1 - level, perlin_noise, level, 0)

    lab_noisy = cv2.merge([l_noisy, a, b])
    return cv2.cvtColor(lab_noisy, cv2.COLOR_LAB2BGR)

def apply_augmentation(image, gaussian_level, perlin_level):
    """ ノイズ適用処理（輝度チャンネルのみに適用） """
    if gaussian_level > 0:
        image = add_gaussian_noise_luminance(image, gaussian_level)
    if perlin_level > 0:
        image = add_perlin_noise_luminance(image, perlin_level)
    return image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_image", type=str, help="入力画像ファイル")
    parser.add_argument("--gaussian_level", type=float, default=0, help="ガウシアンノイズの強度")
    parser.add_argument("--perlin_level", type=float, default=0, help="Perlinノイズの強度")

    args = parser.parse_args()

    if args.input_image:
        clean_image_path = "temp_fixed.png"
        image_path = remove_iccp(args.input_image, clean_image_path)
        if image_path is None:
            return
        image = cv2.imread(image_path)
    else:
        print("入力画像を指定してください。")
        return

    output_image = apply_augmentation(image, args.gaussian_level, args.perlin_level)
    cv2.imwrite("output.png", output_image)
    print("ノイズ画像を保存しました: output.png")

if __name__ == "__main__":
    main()
