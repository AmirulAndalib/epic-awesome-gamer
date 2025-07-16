# 使用更轻量的基础镜像
FROM mcr.microsoft.com/playwright:v1.52.0-noble AS base

# 第一阶段：依赖安装
FROM base AS deps
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 利用 Docker 层缓存，先复制依赖文件
COPY pyproject.toml uv.lock ./

# 安装 Python 依赖
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-cache --all-extras

# 第二阶段：系统依赖
FROM deps AS system-deps

# 安装系统依赖，合并 RUN 命令减少层数
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    xvfb \
    tini \
    wget \
    curl && \
    rm -rf /var/lib/apt/lists/* && \
    # 预先下载 camoufox
    uv run camoufox fetch

# 最终阶段：应用代码
FROM system-deps AS final

WORKDIR /app

# 环境变量
ENV DISPLAY=:99 \
    UV_LINK_MODE=copy

# 最后才复制应用代码（变化最频繁的部分）
COPY . .

# 使用 tini 作为 init 进程
ENTRYPOINT ["/usr/bin/tini", "--"]