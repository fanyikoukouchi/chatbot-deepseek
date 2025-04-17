# DeepSeek 聊天机器人

[English Documentation](README.md)

一个基于 DeepSeek 大语言模型的现代化聊天应用，采用 Vue.js 前端和 Python 后端架构。

## 系统架构

### 概述
系统采用三层架构：
1. 前端 (Vue.js)
2. 后端 (Python FastAPI)
3. DeepSeek API 集成
4. 数据库 (PostgreSQL)

### 数据库
应用使用 PostgreSQL 作为主数据库，具有以下特性：
- 关系型数据库，用于结构化数据存储
- 使用 SQLAlchemy ORM 进行数据库操作
- 连接池支持，提升性能
- 自动迁移支持
- 备份和恢复功能

### 目录结构
```
deepseek-chatbot/
├── frontend/                 # Vue.js 前端应用
│   ├── src/
│   │   ├── components/      # Vue 组件
│   │   ├── views/          # 页面组件
│   │   ├── store/          # Vuex 状态管理
│   │   ├── router/         # Vue Router 配置
│   │   └── api/            # API 服务层
│   └── package.json
├── backend/                 # Python FastAPI 后端
│   ├── app/
│   │   ├── api/            # API 端点
│   │   ├── core/           # 核心业务逻辑
│   │   ├── models/         # 数据模型
│   │   └── services/       # 服务层
│   ├── requirements.txt
│   └── main.py
└── docs/                   # 文档
```

### 技术栈

#### 前端
- Vue.js 3.x
- Vuex 状态管理
- Vue Router 路由管理
- Axios HTTP 请求
- WebSocket 实时通信
- TailwindCSS 样式框架

#### 后端
- Python 3.9+
- FastAPI 框架
- SQLAlchemy ORM
- WebSocket 支持
- JWT 认证
- DeepSeek API 集成

### 主要功能
1. 实时聊天界面
2. 上下文感知对话
3. 工具集成支持
4. 用户认证
5. 对话历史记录
6. 插件系统

### API 设计
后端提供 RESTful API 和 WebSocket 端点：
- `/api/auth/*` - 认证端点
- `/api/chat/*` - 聊天相关端点
- `/ws/chat` - 实时聊天的 WebSocket 端点
- `/api/tools/*` - 工具集成端点

### 安全性
- 基于 JWT 的认证
- HTTPS 加密
- 输入验证
- 速率限制
- CORS 保护

## 开发环境设置

### 前提条件
- Node.js 16+
- Python 3.9+
- DeepSeek API 凭证

### 安装步骤
1. 克隆仓库
2. 设置前端：
   ```bash
   cd frontend
   npm install
   ```
3. 设置后端：
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### 配置
1. 在前端和后端目录创建 `.env` 文件
2. 配置 DeepSeek API 凭证
3. 设置数据库连接

### 运行应用
1. 启动后端：
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
2. 启动前端：
   ```bash
   cd frontend
   npm run serve
   ```

## 性能考虑
- API 响应时间 < 500ms
- WebSocket 连接稳定性
- 前端包优化
- 数据库查询优化
- 缓存策略

## 测试
- 前端：Jest + Vue Test Utils
- 后端：pytest
- 集成测试
- 性能测试

## 部署
- Docker 容器化
- CI/CD 流水线
- 监控和日志
- 备份策略 