# OSにおけるユーザーとは？

OSにログインして，**OSの機能を利用できるユーザのことです。**
Linuxは一般的なオペレーティングシステムと同じで、実際に使用するにはユーザとしてログインする必要がある。ログインに必要なものは「ユーザ名」と「パスワード」が必要になります。  
Linuxでは大まかに「一般ユーザ」と「rootユーザ」に大分できます。  
「rootユーザ」とは管理者権限を持ったOSユーザのことで、OSの環境設定，OSユーザの管理などが可能です。  対して「一般ユーザ」の場合自分専用のディレクトリが割り当てられ、その中で作業をすることになります。  
自分がどのユーザーであるかを確認するコマンドは、
$id
コマンドを使うと確認することが可能です。  
(UID 0がrootユーザ、1から499がシステムユーザ,500以降が個人ユーザ)
_____________________________________________________________________________________________________
# OSにおけるグループとは？

Linuxでは複数人のユーザが同時にアクセスできる為、それらのユーザーを管理する仕組みとして「グループ」という概念があります。  
同一グループのユーザーは、そのグループ所有のファイルに対し、読み込み、書き込み、実行が可能となります。  
また、１アカウントが複数のグループに所属する事も可能です。  
自分がどのグループであるかを確認するコマンドは、$ groups もしくは $ id コマンドで確認することが可能です。
 _____________________________________________________________________________________________________

# ファイル・ディレクトリの権限

 ファイルの権限を確認したい場合、
 $ls -l
 コマンドで確認することができます。

 例えば
```
 -rw-r--r--  1 user user      9  1月 1 00:00 hoge.txt
```
上記のログが表示されていた場合、
左側１０文字はパーミッションを表しています。

１文字目はファイルの種別を表しています。  
２文字目〜４文字目はファイルの所有者に対する権限を表しています。  
５文字目〜７文字目はファイルの所有グループに対する権限を表しています。  
８文字目〜１０文字目はその他に対する権限を表しています。

また、このファイルを読み取り権限のみに変更するには、
chmod コマンドを使い、次にパーミッションを表す英語を入力し最後に対象のファイルを指定します。   
(＄chmod -w hoge.txt)

パーミッションに続く　user userは、左が所有者で右が所有グループを表しています。
