## 概要
Webで簡単に使用できるメモ帳です  
色々な技術を学習するために試行錯誤しながら作成しました  
今後の開発でも活かせるように、バックエンド部分（CRUD、ログイン機能）を意識して設計しました  

## 主な機能
- メモの一覧表示・追加・削除・更新
- ログイン機能
## 対応プラットフォーム
- Windows

## 使用技術
- Python
- Flask
- HTML / CSS
- SQLite
- SQLAlchemy
- Jinja2
- Flask-Login
- Werkzeug
  - werkzeug.security

## 今後の機能改善  
- ユーザーごとにメモを管理
- UIの改善

## 使用方法  
1　Python、Flask、SQLAlchemy、flask-loginをインストール  

2　Python app.pyで起動します

## メモ帳機能の説明
- [ログイン方法](#ログイン方法)
- [メモの追加](#メモの追加)
- [メモの削除](#メモの削除)
- [メモの更新](#メモの更新)
### ログイン方法
#### 1　新規登録ボタンをクリック  
![loginimage](https://github.com/user-attachments/assets/a9a809d8-e679-4b2c-bc98-6ab6feee0020)
#### 2　登録したいユーザーIDとパスワードを入力して登録するをクリック 
![loginimage2](https://github.com/user-attachments/assets/5d005933-65da-4aab-addc-d005d1c49cc7)
#### 3　ログインページに戻るので、登録したユーザーIDとパスワードを入力してログインをクリック  
![loginimage3](https://github.com/user-attachments/assets/042d6cb4-bd15-437a-bef7-0c96bc4b90ab)
#### 4　ログイン完了
![loginimage4](https://github.com/user-attachments/assets/e7c931e6-7b7c-4102-a899-c580f10914e7)
### メモの追加
#### 1　追加したいメモを、追加するの項目に入力して、その右側にある追加ボタンをクリック  
![addimage](https://github.com/user-attachments/assets/bcdcbd95-0f60-45ec-a7de-af95b00b499c)
#### 2　一覧に追加したメモが表示されます  
![addimage2](https://github.com/user-attachments/assets/51b036f7-26d3-4d0a-94a7-965060c1b6fa)

### メモの削除
#### 1　削除したいメモを、削除するのセレクトボックスから選択して、その右側にある削除ボタンをクリック  
![delimage](https://github.com/user-attachments/assets/29255364-d8b1-4423-b457-30af6ac4dfd9)
#### 2　一覧から選択したメモが削除されます
![delimage2](https://github.com/user-attachments/assets/6210697b-2a7b-4ac4-90d8-312a769e9c05)
### メモの更新
#### 1　更新したいメモを、更新するのセレクトボックスから選択して、その右側にある更新ボタンをクリック  
![updateimage](https://github.com/user-attachments/assets/a80201a4-935e-4948-883e-22973ef2956d)
#### 2　更新画面に切り替わるので、更新するの項目に入力して、その右側にある更新ボタンをクリック  
![updateimage2](https://github.com/user-attachments/assets/f4e20fea-9ab6-4662-a88c-1d3bc8a7b382)
#### 3　一覧に更新したメモが表示されます  
![updateimage3](https://github.com/user-attachments/assets/b4cda423-1a23-4532-90c7-c4ed82284d3f)  
