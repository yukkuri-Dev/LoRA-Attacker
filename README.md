# LoRA-Attacker
<p>文字通りLoRAの学習を妨害するPythonscriptです<br></p>
<p>視認性が終わってる？<br>知るか</p>
<h1>利用可能なノイズ</h1>
<h3>ガウシアンノイズ<br>Perlinノイズ</h3>
<h1>How to use</h1> 
<p>ガウシアンノイズ適用<BR>>python AAI.py --input_image [画像のパス] --gaussian_level [強さ] </p>
<p>Perlinノイズ適用<BR>>python AAI.py --input_image [画像のパス] --perlin_level [強さ]</p>
<p>併用<BR>>python AAI.py --input_image [画像のパス] --gaussian_level [強さ] --perlin_level [強さ]</p>
<h3>注意</h3>
<p>あくまで簡易的なものなので対策、もしくは緩和が可能なことに注意してください</p>
<p>Perlinノイズは0.3以下の値を設定することをお勧めします(高くしすぎると画像が目に見えておかしくなります)</p>
<p>ガウシアンノイズは10ほどの値を設定することをお勧めします(高くしすぎるとノイズがひどくなります)</p>
<h1>Setup</h1>
<h2>まずPythonのセットアップを行ってください</h2>
<p>ここからダウンロード https://www.python.org/downloads/</p>
<h2>必要なライブラリの追加</h2>
<p>環境変数設定済みの環境にてこれを実行<br>pip install opencv-python numpy scipy perlin-noise</p>
# MIT License
