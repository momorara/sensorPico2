# sensorPico2
sensorPico version2 for pico

プログラム概要
とりあえず、作成中　個別ライプラリのみです。
オリジナル部分はMIT、それ以外の改変部分については、元のライセンスに従います。

 以下、作成中

<h4><<概要>></h4>
　Raspberry Pi picoWを使った環境測定ボード ver.2<br>
　センサーにAHT10、BMP180(or BMP280)を使用して気温、湿度、気圧を測定します。<br>
　さらにCdsセンサーも搭載して、明暗度も測定できます。<br>
 さらにさらに、人感センサー、超音波測距センサー、赤外線センサー、傾きセンサー、タクトスイッチ増設、ブザーもついてます。<br>
　それらのデータはwifiを使いambientという計測値表示サービスに投げていますので、表示データ保存が可能となっています。<br>
　　*参考サイト==> https://ambidata.io/bd/board.html?id=59777 <br>
　合わせてSWとLEDを２個装着していますので、アイディア次第で色々と使えると思います。<br>
　小型のOLEDディスプレイを装着すれば、ローカルで気温、湿度、気圧を確認することも可能です。<br>
　すべてのソースプログラムを開示いたします。<br>
<br>
・LEDの色等指定はできません。<br>
・部品の仕様が変わる場合があります。 <br>
・基板のバージョンが変わる場合がありますが、機能等に違いはありません。<br>
・ラズパイは付属しません。<br>

<h4><<使用方法>></h4>
git clone https://github.com/momorara/sensorPico2<br>
でパソコンにダウンロードしてください。<br>
インストールについては、インストール文書に従いインストールを行ってください。<br>

<h4><<動作環境>></h4>
2023/8/1 ファームウェア(micropython-firmware-pico-w-130623.uf2)　で動作確認<br>
   
<h4><<使用説明資料>></h4>
説明書類の中の資料を確認ください。
お問い合わせに関しては、購入ページからお願いします。　

<h4><<メンテナンス情報>></h4>
2023/10/29  リポジトリ開設　内容作成中
