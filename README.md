# Pygameカメラ連携ゲームテンプレート / Pygame Camera Game Template

初回更新日: 2026/11/16(月)  
最終更新日: 2026/11/16(月)  

`#Python` `#Pygame` `#OpenCV` `#テンプレート`  
`#Python` `#Pygame` `#OpenCV` `#template`


## 1. 概要

本資料は, `Pygame` と `OpenCV` を組み合わせたゲーム制作テンプレートの簡易リファレンスです.  
Webカメラ映像の取得と画面描画, キー入力管理, およびシーン遷移の基本構造を提供します.  
本テンプレートをベースに各シーンの処理を実装することで, カメラ映像を活用したゲームやインタラクティブ作品を素早く開発できます.  


## 2. セットアップ

### 2.1. 必要ライブラリ

- `Python` (3.x系)
- `pygame`
- `opencv-python`

### 2.2. インストールと起動

必要なパッケージをインストールします.  

```bash
pip install pygame opencv-python
```

## 3. ディレクトリ構成

本テンプレートの基本構成は以下の通りです.  

```text
project_root/
├─┬ assets/                     # アセット
│ ├── bgms/                     # 音楽 / BGM
│ ├── images/                   # 画像
│ ├── models/                   # 画像検出モデルなど
│ └── sounds/                   # 効果音
├── docs/                       # アセット
│   └─ template-archtecture.md  # クラス図やアーキテクチャーの説明
├── main.py                     # エントリーポイント
├── modules/
│   ├── animation_time.py       # アニメーション時間・進捗管理
│   ├── camera.py               # Webカメラ制御
│   ├── event.py                # Pygameイベント取得
│   ├── frame_converter.py      # OpenCV画像からPygame Surfaceへの変換
│   ├── game.py                 # メインループ・全体統括
│   ├── game_data.py            # 共有設定・状態保持
│   ├── game_scene.py           # ゲーム本編シーン
│   ├── input.py                # キー押下状態管理
│   ├── keys.py                 # キー定義Enum・変換
│   ├── scene.py                # シーン基底クラス
│   ├── scene_manager.py        # シーン切り替え管理
│   ├── title_scene.py          # タイトル画面シーン
│   ├── ui_compornents.py       # 共通UI描画関数
│   └── window.py               # ウィンドウ生成・描画統括
└── README.md                   # README
```

