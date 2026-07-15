# 网站模板与 UX 架构规划

## 当前阶段边界

本文件用于规划“脑机接口与有源植入式医疗器械测试设备中文站”的页面模板、信息架构、组件系统和询盘路径。

当前阶段只做规划，不连接服务器，不连接 WordPress，不连接测试站，不修改现有网站，不改 DNS，不发布页面，不创建 301，不生成完整产品页面。

## 网站定位

本网站定位为：脑机接口与有源植入式医疗器械测试设备研发方向展示站 + 技术能力介绍站 + 定制开发询盘站。

第一阶段 20 个方向仍按“研发中 / 技术预研 / 可定制开发评估 / 需要人工确认”处理。页面模板必须支持研发状态提示、标准映射待确认、参数待确认和技术询盘。

## 竞品与同行学习边界

同行网站、Fluke Biomedical、WhaleTeq 等公开资料只能用于信息架构、页面模块、视觉层级、技术内容呈现方式和 B2B 询盘路径参考。不得复制同行文案、图片、参数、页面布局、HTML/CSS、品牌表达或产品事实。

## 推荐视觉风格方向

- 专业医疗工程风格：清晰、克制、可信，避免消费级医疗广告感。
- 技术实验室风格：突出测试系统、夹具、信号链路、标准映射和实验室验证场景。
- 高密度但有层次：适合研发、法规、检测机构用户快速扫描标准、对象、测试项目和确认状态。
- 主色建议：深蓝/墨蓝用于信任感，青蓝或绿色作技术强调色，浅灰/白色作内容背景，少量橙色用于“需要确认/注意”状态。
- 字体与版式：中文正文重视可读性，H1 简洁；表格、卡片、状态标签和模块标题保持稳定尺寸。

## 不推荐的模板风格

- 大幅营销落地页、空泛 Hero、夸张渐变、装饰性过强的科技感背景。
- 只展示产品图和参数表的传统目录站模板。
- 过度花哨的 Elementor 动画模板。
- 医疗诊疗、临床疗效或患者故事导向模板。
- 会暗示“现货产品”“认证通过”“临床应用”的电商型产品模板。

## WordPress 实现建议

- 不建议当前阶段购买重型商业主题作为核心依赖。可后续选择轻量、可维护、兼容 Gutenberg/ACF 的主题框架。
- 建议优先使用 Gutenberg + ACF 自定义字段 + 自定义模板。
- Elementor 可用于少量营销/联系页面，但不建议作为全部产品与标准内容的核心数据层。
- 产品方向页、标准页、PDF 下载页建议使用 ACF 字段管理来源、研发状态、标准映射、参数确认状态和 CTA。

## 页面模板规划

### 1. Home Page Template

- Page Purpose: 建立医疗专站定位，说明 KingPo 在医疗测试设备、标准测试设备、研发验证和定制开发方面的基础能力。
- Target User: 医疗器械研发、注册检验、第三方检测、企业实验室、采购和法规人员。
- Search Intent: 了解 KingPo 是否具备 BCI / 有源植入式 / 医疗电气测试设备方向能力。
- Recommended H1 / Hero Structure: H1 使用“脑机接口与有源植入式医疗器械测试设备”；副标题说明研发验证、标准映射和定制开发询盘。
- Main Content Sections: 核心方向、KingPo 现有能力、第一批研发方向、标准体系、测试场景、资料下载、技术询盘。
- Required Modules: Hero Section、Core Information Cards、R&D Status Notice、Related R&D Directions、Standard Mapping Module、Technical Inquiry CTA。
- CTA Position: Hero 右侧/下方、核心方向后、页面底部固定技术询盘区。
- Internal Link Strategy: 链接产品分类、标准页、技术文章、PDF 下载、联系页。
- Image Requirements: 医疗测试实验室场景、系统概念图、KingPo 现有设备图或合规生成图；避免临床患者图。
- SEO Notes: 聚焦“脑机接口测试设备”“有源植入式医疗器械测试设备”“医疗电气安全测试设备”。
- Compliance / Overclaim Risk Notes: 不写已完全符合标准，不写 20 个方向为现货。
- Mobile Layout Notes: Hero 文案压缩为 2-3 行；核心卡片单列；CTA 保持可触达。

### 2. Product Category Page Template

- Page Purpose: 汇总某一医疗测试设备方向下的研发方向、已有能力、相关标准和询盘入口。
- Target User: 按产品类别寻找测试设备的采购、研发和检测人员。
- Search Intent: 查找某类测试设备或测试方案。
- Recommended H1 / Hero Structure: H1 使用类别名，如“有源植入式医疗器械测试设备”；Hero 中明确“研发方向与定制开发评估”。
- Main Content Sections: 类别概述、适用对象、相关标准、方向卡片、KingPo 背景能力、FAQ、询盘。
- Required Modules: Core Information Cards、R&D Status Notice、Standard Mapping Module、Related R&D Directions、FAQ Module、Technical Inquiry CTA。
- CTA Position: 方向卡片后和页面底部。
- Internal Link Strategy: 链接子方向页、标准页、知识页、PDF 下载页。
- Image Requirements: 类别级系统图、实验室图、测试对象示意图。
- SEO Notes: 类别关键词 + 标准号 + 研发验证场景。
- Compliance / Overclaim Risk Notes: 分类页可说“方向”，不要列未经确认的成熟型号。
- Mobile Layout Notes: 分类卡片单列；标准映射表可横向滚动或折叠。

### 3. R&D Direction Page Template

- Page Purpose: 展示一个研发/预研/定制评估方向的测试对象、标准映射、可能测试项目和询盘确认路径。
- Target User: 对某个具体测试方向有需求的研发、法规、实验室用户。
- Search Intent: 查找具体测试方向，如 EEG 闭环测试、除颤兼容、TMS 兼容。
- Recommended H1 / Hero Structure: H1 使用方向名；Hero 立即显示“研发方向 / 参数待确认 / 可定制评估”。
- Main Content Sections: 一句话定位、核心信息、研发状态、标准映射、测试对象、测试项目、参数待确认、系统图、选型问题、FAQ、询盘。
- Required Modules: R&D Status Notice、Technical Parameters Pending Confirmation Module、Standard Mapping Module、Test Object Module、Test Item Module、System Diagram Module、Technical Inquiry CTA。
- CTA Position: 核心信息后、参数待确认模块后、页面底部。
- Internal Link Strategy: 链接所属分类、相关标准、相关研发方向和资料下载。
- Image Requirements: 占位系统概念图、测试链路图、可公开设备/夹具图片；不得用未批准内部图。
- SEO Notes: 允许写方向关键词和标准映射方向，但不写“现货”“通过认证”。
- Compliance / Overclaim Risk Notes: 必须显示研发状态和人工确认状态。
- Mobile Layout Notes: 研发状态提示置顶；长表格改为卡片式字段。

### 4. Standard / Knowledge Page Template

- Page Purpose: 按标准号解释其与测试设备方向的关系，帮助用户从标准找到相关测试方向。
- Target User: 法规、质量、注册检验、第三方检测人员。
- Search Intent: 查询 ISO 14708、YY/T 1996、IEC 60601 等标准相关测试设备。
- Recommended H1 / Hero Structure: H1 使用“ISO 14708 有源植入式医疗器械测试设备方向”等谨慎表述。
- Main Content Sections: 标准概述、适用对象、可能测试方向、相关研发设备、证据状态、FAQ、询盘。
- Required Modules: Related Standards Module、Standard Mapping Module、Related R&D Directions Module、FAQ Module。
- CTA Position: 标准映射后和底部。
- Internal Link Strategy: 标准页互链、链接相关 R&D 方向和技术文章。
- Image Requirements: 标准映射图、测试对象关系图。
- SEO Notes: 标准号 + 测试设备 + 测试方向。
- Compliance / Overclaim Risk Notes: 不解释未确认条款，不声称 KingPo 产品覆盖全部标准。
- Mobile Layout Notes: 标准表格折叠；先给结论卡片。

### 5. Technical Article Page Template

- Page Purpose: 用原创中文技术内容解释测试原理、选型问题和研发验证方法。
- Target User: 研发、检测、法规和实验室工程师。
- Search Intent: 学习测试方法、标准背景、选型注意事项。
- Recommended H1 / Hero Structure: H1 以问题或方法命名，如“脑机接口闭环测试需要确认哪些信号参数”。
- Main Content Sections: 问题背景、测试对象、方法说明、标准映射、资料来源、相关方向、FAQ。
- Required Modules: Related Standards Module、Test Object Module、Test Item Module、Technical Inquiry CTA。
- CTA Position: 文章中段和底部。
- Internal Link Strategy: 链接相关 R&D 页、标准页、PDF 下载页。
- Image Requirements: 流程图、框图、测试链路图；优先原创示意。
- SEO Notes: 长尾关键词和问题型关键词。
- Compliance / Overclaim Risk Notes: 不写未经确认的参数和结论。
- Mobile Layout Notes: 目录锚点、短段落、图表可缩放。

### 6. Case Study Page Template

- Page Purpose: 后续展示已获批准的应用案例或测试方案示例。
- Target User: 采购、研发经理、实验室负责人。
- Search Intent: 了解 KingPo 是否有相关项目经验。
- Recommended H1 / Hero Structure: 使用“某类测试方案案例”而非客户名，除非获授权。
- Main Content Sections: 项目背景、测试需求、方案模块、结果范围、保密说明、相关设备、询盘。
- Required Modules: R&D Status Notice、System Diagram Module、Image Gallery Module、Technical Inquiry CTA。
- CTA Position: 方案模块后和底部。
- Internal Link Strategy: 链接相关方向页和标准页。
- Image Requirements: 只使用获批准案例图；无授权时用匿名系统示意图。
- SEO Notes: 可做行业应用长尾，不虚构客户。
- Compliance / Overclaim Risk Notes: 客户名、结果、认证、交付状态必须来源确认。
- Mobile Layout Notes: 时间线或方案卡片单列。

### 7. PDF Download Page Template

- Page Purpose: 汇总可公开 PDF、目录、选型表和技术资料下载。
- Target User: 采购、研发、法规和实验室用户。
- Search Intent: 下载资料、目录、选型表。
- Recommended H1 / Hero Structure: H1 使用“医疗测试设备资料下载”。
- Main Content Sections: 下载分类、PDF 卡片、适用方向、资料来源、版本/日期、询盘。
- Required Modules: PDF Download Module、Related R&D Directions Module、Technical Inquiry CTA。
- CTA Position: 每个下载卡片旁和底部。
- Internal Link Strategy: PDF 链接回产品方向、标准页和联系页。
- Image Requirements: PDF 封面缩略图或文件类型图标。
- SEO Notes: PDF 页面需有可索引说明文字，不只放文件列表。
- Compliance / Overclaim Risk Notes: 只放获批准公开的 PDF；旧资料需标注参考状态。
- Mobile Layout Notes: 下载卡片单列，文件大小和日期清晰。

### 8. Contact / Inquiry Page Template

- Page Purpose: 收集定制开发、标准测试、样品对象和技术参数需求。
- Target User: 有明确测试需求的采购、研发和实验室用户。
- Search Intent: 联系厂家、询价、咨询方案。
- Recommended H1 / Hero Structure: H1 使用“医疗测试设备技术询盘”。
- Main Content Sections: 表单、询盘前需准备信息、联系方式、响应流程、隐私说明。
- Required Modules: Technical Inquiry CTA、Core Information Cards。
- CTA Position: 页面主体即表单；底部补充联系方式。
- Internal Link Strategy: 从所有 R&D 页、标准页、PDF 页导入。
- Image Requirements: 简洁实验室或工程团队图，不使用医疗治疗场景。
- SEO Notes: 品牌 + 技术询盘 + 医疗测试设备。
- Compliance / Overclaim Risk Notes: 表单不承诺交期、库存或认证结果。
- Mobile Layout Notes: 表单字段分组，减少一次性输入压力。

## 通用页面组件库

### Hero Section

用于明确页面定位、研发状态和主 CTA。研发方向页 Hero 必须显示“研发方向 / 参数待确认 / 可定制开发评估”。

### Core Information Cards

用于展示标准方向、测试对象、测试目的、数据来源和人工确认状态。卡片数量建议 4-6 个。

### Standard Mapping Module

展示标准号、组织、相关性、Page Use、证据来源和是否需要人工确认。不得写未经确认版本和条款。

### Test Object Module

列出设备可能服务的样品对象，如 BCI 系统、神经刺激器、IPG、电极、导线、组织接口网络等。

### Test Item Module

列出可能测试项目，并按“已确认 / 需要确认 / 研发参考”标记。

### R&D Status Notice

明确显示：当前方向属于研发中、技术预研、可定制开发评估或需要人工确认，不得作为现货产品理解。

### Technical Parameters Pending Confirmation Module

在参数未确认时替代传统参数表，提示客户提供样品、标准、信号、电气、机械、磁场、超声或 EMC 条件。

### System Diagram Module

用于展示测试链路、信号流、样品连接和数据记录流程。优先原创框图，不复制同行图纸或软件界面。

### Image Gallery Module

用于展示获批准图片，包括设备图、夹具图、实验室图、PDF 封面和示意图。

### Related Standards Module

展示相关标准族，不声明完全符合，仅说明标准映射方向和确认状态。

### Related R&D Directions Module

连接 20 个研发方向中的相关页面，避免孤立页面。

### FAQ Module

围绕标准适用性、样品对象、参数确认、定制开发、资料下载和询盘准备问题。

### PDF Download Module

展示可公开 PDF，字段包括资料名称、适用方向、来源、版本/日期、公开状态。

### Technical Inquiry CTA

引导用户提交标准号、样品对象、测试项目、参数范围、是否需要定制夹具和可公开资料。

## 第一批需要设计的 5 个关键页面

1. 首页：建立医疗专站定位和技术能力入口。
2. 有源植入式医疗器械测试设备分类页：承载 ISO 14708 和 AIMD 总方向。
3. 脑机接口测试设备 R&D 方向页：承载 BCI 总方向和闭环测试入口。
4. EEG 动态模拟闭环测试仪 R&D 方向页：适合作为相对清晰的样板页候选。
5. 医疗测试设备技术询盘页：承接定制开发和参数确认。

## 第一批需要准备或生成的图片清单

1. 首页 Hero 医疗测试实验室场景图。
2. BCI 测试系统概念图。
3. 有源植入式医疗器械测试链路框图。
4. EEG 动态模拟闭环测试流程图。
5. 标准映射示意图。
6. 技术参数待确认模块占位图。
7. PDF 下载资料封面缩略图模板。
8. KingPo 现有医疗测试设备图片整理清单。

## 下一步

下一步应先建立可公开图片清单、PDF 清单、KingPo 现有医疗测试设备页面清单和第一批 5 个页面的字段表。仍不开发、不安装主题、不连接 WordPress。