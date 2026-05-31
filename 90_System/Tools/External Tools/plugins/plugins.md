# plugins

用途：个人 Codex plugin 托管入口。

## Jarvis 托管路径

```text
<jarvis-root>/90_System/Tools/External Tools/plugins/root
```

## 当前插件

| Plugin | 入口 |
|---|---|
| production-readiness | [[production-readiness/production-readiness|production-readiness]] |

## Marketplace

个人 marketplace 文件仍在：

```text
~/.agents/plugins/marketplace.json
```

当前 marketplace 中有 `production-readiness` 条目，其本地路径指向 Jarvis 托管仓库。

旧入口 `~/plugins` 已删除，不再作为兼容路径保留。

## 验证

```bash
test -d "<jarvis-root>/90_System/Tools/External Tools/plugins/root"
test -L "<jarvis-root>/90_System/Tools/External Tools/plugins/root/production-readiness"
```
