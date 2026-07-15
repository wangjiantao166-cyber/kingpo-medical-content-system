# KingPo 现有官网资料来源清单

## 当前阶段边界

本文件记录 KingPo / DGKingPo 现有公开官网中可作为第一批基础资料层的来源类型和建议使用方式。

当前阶段仅做公开资料来源规划和页面类型审计，不登录后台，不连接服务器，不修改现有网站，不复制页面内容，不发布页面。

## 来源分级

- P0: KingPo 已有官网 / PDF / 图片 / 内部确认资料
- P1: 官方标准 / 标准映射资料
- P2: 用户后续补充资料
- P3: 同行参考，仅用于结构学习和测试项目理解，不作为 KingPo 产品事实来源

## 已确认可参考的 KingPo 公开资料类型

| 来源 | URL | 可参考内容 | 可支持的新站内容 | 限制 |
| --- | --- | --- | --- | --- |
| DGKingPo 首页 | https://www.dgkingpo.com/ | 品牌入口、产品分类、B2B 询盘路径 | 首页信息架构、导航、CTA 思路 | 不直接复制文案或布局 |
| DGKingPo Medical Test Equipment 分类页 | https://www.dgkingpo.com/product-category/medical-test-equipment/ | 医疗测试设备分类、产品卡片、图片、FAQ、询盘入口 | 医疗测试设备基础能力、分类页模块、产品卡片模式 | 不能证明 20 个新方向均为现货 |
| ECG Electrode Performance Tester | https://www.dgkingpo.com/product/ecg-electrode-performance-tester/ | ECG 电极性能测试、产品图、PDF、FAQ、询盘路径 | 电极测试、ECG、医疗电气测试背景能力 | 参数、标准和成熟度需按页面和资料核实，不迁移为新方向参数 |
| IEC 60601-2-4 Defibrillation Electrode Performance Tester | https://www.dgkingpo.com/product/iec-60601-2-4-defibrillation-electrode-performance-tester/ | 除颤电极、IEC 60601-2-4 方向、产品图、PDF、FAQ | 除颤兼容、电极性能、医疗安全测试背景能力 | 不等同于植入式器械除颤兼容测试仪已成熟 |
| ESU Analyzer / Electrosurgical Unit Tester | https://www.dgkingpo.com/product/esu-analyzer-electrosurgical-unit-tester/ | ESU / 高频电刀测试方向、医疗电气测试页面结构 | 医疗电气安全、测试设备表达、PDF/FAQ/CTA 模块 | 不作为 BCI/AIMD 新方向参数来源 |
| Implantable Surge Generator | DGKingPo 医疗测试设备分类页中可见产品方向 | 植入式浪涌/医疗电气冲击方向线索 | 植入式器械、电气冲击、兼容性背景能力 | 需进一步核对产品页和 PDF，不能推断参数 |
| KingPo.hk | https://www.kingpo.hk/ | KingPo 旧资料、品牌和产品线线索 | 辅助核对来源 | 需逐页核对，当前不全站采集 |
| batterytestingmachine.com | https://www.batterytestingmachine.com/ | 历史产品站、B2B 页面结构 | 页面结构参考，当前非第一阶段主线 | 不作为医疗专站主线资料 |
| KingPo PDF catalog | 待用户提供或从官网逐项核对 | PDF 风格、产品资料结构、下载模块 | PDF 下载页、资料卡片、产品资料字段 | 未确认 PDF 不公开复用 |
| KingPo 产品图片 | 官网公开图片 / 待授权内部图 | 设备图、夹具图、实验室图、PDF 封面 | 视觉资产、图库、Hero/模块图片 | 需确认版权、清晰度、是否适合新站 |
| KingPo 成功案例 | 待用户确认 | 已交付案例、应用场景 | Case Study 模板 | 客户名、结果、认证、交付状态必须授权确认 |
| KingPo 标准页面和技术文章 | 待逐页核对 | 标准号、测试方法、FAQ、应用场景 | 标准页和技术文章结构 | 不编造标准版本和条款 |

## 可提取或学习的内容

### 可作为 P0 背景能力的内容

- KingPo 已有医疗测试设备分类基础
- KingPo 已有 IEC 60601、ECG、除颤电极、ESU、医疗电气安全相关页面基础
- KingPo 已有产品图、PDF 下载、FAQ、询盘 CTA、产品图库等 B2B 页面模块
- KingPo 已有标准测试设备和医疗电气测试设备表达方式

### 可用于新中文站模板的内容

- 分类页卡片结构
- 产品详情页基本模块顺序
- PDF 下载位置和表现方式
- FAQ 模块
- 询盘路径和按钮位置
- 产品图片和图库组织方式
- 标准号和测试对象的基础呈现方式

### 不得直接推断的内容

- 第一阶段 20 个研发方向已经成熟可售
- 20 个方向已有样机或已交付
- 20 个方向已通过认证或完全符合标准
- 未确认标准版本、条款号、测试条件、参数范围
- 未授权客户案例、成功案例、价格、库存、交期

## 第一轮低频采集范围建议

第一轮只建议审计：

1. DGKingPo 首页
2. Medical Test Equipment 分类页
3. ECG Electrode Performance Tester 页面
4. IEC 60601-2-4 Defibrillation Electrode Performance Tester 页面
5. ESU Analyzer / Electrosurgical Unit Tester 页面
6. 医疗分类页中与植入式、电极、ECG、除颤、医疗电气安全相关的 5-10 个代表页面
7. 对应 PDF 下载链接和图片主题

不进行全站爬取，不高频请求，不访问后台。