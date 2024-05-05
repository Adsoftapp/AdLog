# AdSoftApp/AdLog
## 一个由 AdSoftapp 打造的基于 Python 的日志记录器
### 优点
- 能使用**6个时间服务器**来决定时间。当1个时间服务器不能用的时候，另一个时间服务器会帮忙。那几个时间服务器分别是 `time.windows.com`（微软）、`pool.ntp.org`（志愿者）、`time.apple.com`（苹果）、`time.nist.gov`（美国国家标准与技术研究所（NIST））、`time.amazon.com`（亚马逊）。**[分先后顺序]** ~~目前还有点问题~~
> [!IMPORTANT]
> 当6个时间服务器都同步不上的或计算机已离线的时候，时间将会使用**本地时间**
- 不再使用 Python 自带的 `logging` 库，使用自制的时间格式：`年/月/日 时(24时制):分(60分制):秒(60秒制)`
