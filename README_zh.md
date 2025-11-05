# 🌾 星露谷风格连连看小游戏



> 一款使用 **Python + Pygame** 开发的星露谷风格休闲益智游戏，采用图结构与 BFS 算法实现图块连通判定，支持多主题、计分排行、提示与重排等功能。  

> 现已支持 **Windows 可执行文件 (.exe)**，无需安装 Python 即可游玩。



---



## 🎮 项目简介



本项目是一个基于数据结构与算法课程的综合实践，通过实现“连连看”玩法，掌握二维数组、图结构和广度优先搜索（BFS）在游戏逻辑中的应用。  

游戏整体风格参考《星露谷物语》，界面清新、玩法丰富，既能锻炼算法思维，也能放松娱乐。



---



## 🌟 主要功能



- 图结构 + BFS 实现图块连通判定  

- 提示 / 重排 / 计时 / 计分 / 暂停 / 排行榜 / 设置 / 帮助  

- 模块化架构，界面与逻辑解耦  

- 提供 EXE 可执行文件，无需配置环境



<p align="center">

  <img src="./screenshots/1.png" width="300">

  <img src="./screenshots/2.png" width="300">

  <img src="./screenshots/3.png" width="300">

  <img src="./screenshots/4.png" width="300">

  <img src="./screenshots/5.png" width="300">

</p>



---



## 📂 项目结构



StardewValleyLinkingGame/

├── Main.py # 程序入口

├── UI/ # 界面模块

│ ├── Menu.py

│ ├── Game.py

│ ├── GameLevel.py

│ ├── GamePic.py

│ ├── Ranking.py

│ ├── Settings.py

│ └── Help.py

│

├── Game/ # 游戏逻辑模块

│ ├── constants.py

│ ├── Control.py

│ └── Logic.py

│

├── assets/ # 图片与音效

├── screenshots/

├── DISCLAIMER.md

└── README.md



---



## 🕹️ 运行方法



### ✅ 方法一：运行 EXE（推荐）

1. 👉 下载最新版本：https://github.com/SummerNeverEnds/StardewValleyLinkingGame/releases

2. 双击即可开始游戏，无需安装 Python  



### 💻 方法二：克隆到本地后自行运行源码（python Main.py）

