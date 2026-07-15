# AGENTS.md

## Repository Purpose

This repository is the KingPo multi-site content operating system for product master data, source evidence, WordPress publishing, SEO architecture, visual assets, and release quality control.

## Platform Routing

```yaml
default_implementation_platform: wordpress

wordpress_routes:
  content_model: wordpress-content-model-admin
  presentation: wordpress-theme-template
  operations: wordpress-operations-deployment

disabled_by_default:
  - nextjs-content-model-admin
  - nextjs-template-rendering-system
```

Agents generate and modify code, schemas, reports, drafts, and deployment plans. WordPress is the content operations system. WP-CLI is the primary automation interface. REST API use must be explicitly allowed for a specific operation. Direct SQL writes to production content are prohibited. All production changes pass through `release-quality-gate`; standards and technical claims still require human review.

It is based on the earlier Chinese website rebuild planning repository, but extends it into a maintainable product publishing system for:

- structured product records
- WordPress custom post types and ACF fields
- product lifecycle status and site targeting
- field-level source and claim evidence
- application and test-scenario pages
- standard relationship review
- internal linking architecture
- image and PDF asset governance
- inquiry conversion
- product publish QA
- ongoing content refresh
- import/export workflows

The target is a KingPo-specific B2B product knowledge system with strong catalog depth and internal linking, inspired by mature equipment-industry information architecture patterns, while keeping all KingPo content original, source-based, and cautious with technical, standards, medical, and regulatory claims.

## Existing Company Source Context

KingPo should not be described as only a medical device testing company. Existing source material mainly comes from:

- https://www.dgkingpo.com/ as the KingPo / DGKingPo main site and broad test equipment source
- https://www.batterytestingmachine.com/ as a KingPo English product site covering battery testing equipment, environmental test chambers, safety compliance testing equipment, and related medical test equipment categories
- https://www.kingpocn.com/ as a KingPo domestic Chinese site and Chinese-market source. It may support Chinese product facts, category understanding, images, and company capability references, but English/export content should be rewritten for overseas B2B buyers instead of directly machine-translated.
- https://www.kingpo.hk/ as a KingPo-related site that must be recorded in the source registry when page-level content is reviewed. If unavailable or unstable, do not infer facts from it.

The content system should use these sites as KingPo-owned or KingPo-related source references where relevant, while still recording exact page-level sources and human verification status.

## Project

This repository is for building a KingPo product and content operating system that can serve multiple WordPress publishing targets and languages.

Project positioning:

KingPo 多站共用产品主数据与外贸内容系统

KingPo Multi-Site Product Data and B2B Content Operating System

The goal is to create a professional source-based system for product display, product inquiries, technical content, standards-based pages, application scenarios, laboratory use cases, and SEO growth across KingPo product domains.

WordPress is the first-stage publishing layer. Do not migrate, replace, redirect, publish to, or modify any existing production website unless the user gives explicit approval.

## First-Phase Scope

The first phase focuses on system architecture, data contracts, evidence rules, WordPress implementation specifications, SEO architecture, and agent coordination before mass content production.

Priority product domains may include:

- Medical Device Test Equipment
- Battery Safety Test Equipment
- Environmental & IP Test Equipment
- Electrical Safety Test Equipment
- Flammability & Material Test Equipment
- Plug, Socket, Cable & Gauge Test Equipment
- Automotive & EV Test Equipment
- Automation & Custom Test Systems

Medical products remain an important vertical. BCI, active implantable medical device test equipment, medical electrical safety, medical gauges, ISO 80369, ISO 18250, and luer connector test equipment should be handled when supported by source evidence and business priority, but they do not define the entire repository.

## Critical Rules

Do not modify the production website directly.

All development work must first be done in a staging or test environment.

Do not change DNS records without approval.

Do not publish pages without approval.

Do not create 301 redirects for the current phase.

Do not delete, replace, or change old website URLs.

Do not invent product specifications, standards, certifications, customer names, test capabilities, prices, stock status, delivery time, regulatory approval, registration status, clinical claims, or R&D completion status.

All key technical information must be based on verified sources such as uploaded spreadsheets/PDF lists, approved company websites, product documents, PDF catalogs, images, or confirmed user input.

If product data is unclear, conflicting, or only a roadmap item, mark it as “需要人工确认” or “研发参考 / 需要人工确认”.

Do not publish R&D reference products as available KingPo stock products unless confirmed by the user.

Standards must not be invented. If existing materials are incomplete, agents may consult official or authoritative standards sources such as IEC, ISO, EN/CEN/CENELEC/ETSI, UL, UN ECE, SASO, BIS, ANSI/AAMI, ASTM, and IEEE for public standard titles, scope, standard families, and high-level relevance. Agents must not invent versions, clause numbers, test conditions, acceptance criteria, or KingPo compliance conclusions.

## Source Ownership Rule

Source ownership must be clearly classified before product data is used.

First-phase core product roadmap sources:

- User-uploaded spreadsheets and PDF lists for BCI, active implantable medical device, neural stimulation, implantable pulse generator, signal simulation, compatibility, electrode, lead, insulation, withstand voltage, tissue interface, and related medical testing equipment.
- User-confirmed product lists, standard mappings, product specifications, images, diagrams, and PDF catalogs.

Owned or priority sources:

- dgkingpo.com
- kingpo.hk
- batterytestingmachine.com, historical source only and not a first-phase priority
- syrianetf.com, old-material reference only and not a production target

Owned or priority sources may be used as KingPo product fact sources, but key technical parameters must still be marked with their source.

Competitor reference sources:

- sinuotek.com
- lisungroup.com
- bndtestequipment.com
- iectestingequipment.com
- haidatestequipment.com
- china-gauges.com
- Fluke Biomedical / 福禄克 public materials
- WhaleTeq / whaleteq.com / https://www.whaleteq.com/zh-tw public materials
- Other public medical testing equipment and active implantable medical device testing references

Competitor reference sources may only be used for market learning, product classification, page structure, FAQ direction, user needs, R&D reference, product roadmap reference, and content strategy. They must not be used as KingPo product parameters, certifications, customer cases, images, or product fact sources.

## Competitor Benchmark Rule

Codex may study public competitor information, including Fluke Biomedical / 福禄克医疗检测设备相关公开资料 and WhaleTeq / whaleteq.com medical electrical safety and medical test equipment public materials, only for lawful benchmarking, market understanding, product roadmap reference, R&D learning, and content strategy.

Competitor information must not be copied, republished, imitated too closely, or used to make unsupported KingPo product claims.

If a competitor has a product that KingPo does not currently sell, mark it as “研发参考 / 需要人工确认”. Do not publish it as an available KingPo product unless confirmed by the user.

Do not claim equivalence such as “same as Fluke”, “Fluke replacement”, “Fluke equivalent”, “better than Fluke”, “WhaleTeq 替代品”, “同款 WhaleTeq”, “完全等同 WhaleTeq”, “WhaleTeq replacement”, or “WhaleTeq equivalent” unless verified test data and legal approval exist.

## Legacy Medical Vertical Notes

The following medical Chinese-site notes are retained as a legacy vertical reference. Use them only when the task is specifically about a Chinese medical testing equipment section or prototype. They must not override the v2 system scope in `docs/00-system-scope-and-sites.md`.

For that vertical, the website may serve Chinese-speaking B2B medical test equipment customers, including:

- 脑机接口研发团队
- 有源植入式医疗器械厂家
- 神经刺激器和植入式脉冲发生器研发团队
- 起搏器 / ICD 相关研发和检测团队
- 医疗器械注册检验机构
- 第三方检测机构
- 医疗器械企业实验室
- 高校、医院和科研单位
- 质量、法规、可靠性和研发验证部门

The content should be professional, source-based, cautious with medical and regulatory claims, and suitable for Chinese procurement, R&D, registration testing, and laboratory users.

## Legacy Medical Product Page Structure

When producing a Chinese medical product page, this older structure may be used as a starting point, but it should be adapted to the product, source completeness, buyer intent, and the flexible page-brief rules in `docs/content-types-and-acf-field-map.md`:

1. H1
2. 一句话产品定位
3. 核心信息
4. 产品概述
5. 适用标准与条款方向
6. 测试原理
7. 测试对象与样品类型
8. 测试项目
9. 技术参数
10. 典型应用
11. 研发验证 / 注册检验 / 第三方检测场景
12. 选型与配置建议
13. 相关产品
14. 常见问题
15. 询盘 CTA

The “核心信息” section must appear before “产品概述”.

Do not write thin, generic, or keyword-stuffed content.

## Legacy Medical SEO Notes

When working specifically on the medical Chinese vertical, SEO may focus on BCI test equipment, active implantable medical device test equipment, medical electrical safety, neural stimulation testing, implantable medical device testing, relevant GB / YY / ISO standards, signal simulation, compatibility testing, and procurement or R&D validation intent.

Priority SEO directions include:

- 脑机接口测试设备
- 有源植入式医疗器械测试设备
- 医疗电气安全测试设备
- 神经刺激器测试设备
- 植入式医疗器械测试设备
- YY/T 1996 测试设备
- GB 16174 测试设备
- YY 0989 测试设备
- ISO 14708 测试设备
- EEG / EMG / EOG / LFP / Spike / ECoG 信号模拟
- 除颤兼容测试
- TMS 兼容性测试
- 超声兼容测试
- EMC 抗扰度测试

For every important page, prepare H1, SEO Title, Meta Description, URL Slug, core keywords, related keywords, image filename suggestions, image alt text, internal link suggestions, FAQ, and Schema suggestions.

## Legacy Medical Sample Pages

These earlier sample pages are retained as possible medical fixtures or future examples, not as the mandatory first-phase roadmap for the whole repository:

1. 脑机接口测试设备
2. 有源植入式医疗器械测试设备
3. 电生理动态模拟闭环测试仪
4. EEG 动态模拟闭环测试仪
5. 头部植入器械综合应力模拟测试仪
6. 经皮能量传递测试仪
7. 植入式医疗器械除颤兼容测试仪
8. 大功率电场模拟器
9. 超声兼容测试仪
10. 有源植入式器械机械应力综合测试套件
11. 压力循环测试系统
12. 电极耐压自动测试仪
13. 静磁场测试系统
14. 时变磁场测试仪
15. 心律管理器械低频电磁抗扰度测试仪
16. 多通道光纤检测仪
17. 神经刺激器电极组织接口网络模块
18. IPG 注入测试系统
19. 植入器械 TMS 兼容性测试仪
20. 超声脑机接口性能测试仪

## Allowed Work

Codex may help with website architecture, product category planning, Chinese product page drafts, SEO metadata, image alt text, FAQ, internal link suggestions, WordPress theme or plugin planning, ACF field planning, product template planning, QA checklist, staging deployment support, source record planning, and lawful competitor benchmarking for medical testing equipment market learning and R&D reference.

## Restricted Work

Codex must not do the following without explicit approval:

Modify the production website
Publish pages
Change DNS
Delete pages
Change URL structures
Create 301 redirects
Install or remove plugins on the production website
Modify production theme code
Modify production database
Change inquiry form email settings
Bulk import products
Bulk redirect URLs
Copy competitor text, images, tables, manuals, PDFs, drawings, screenshots, software interfaces, layouts, trademarks, customer cases, or certification claims
Copy competitor model naming systems
Use competitor data as KingPo product facts
Claim KingPo has unconfirmed competitor-style products or functions
Write R&D reference products as KingPo existing stock products

## Agent Collaboration

Use the following agent roles when needed:

Master Agent
SEO & Architecture Agent
Product Data Agent
WordPress Developer Agent
Content Rewrite Agent
Competitor Benchmark and R&D Learning Agent
QA Agent
Security Agent

Additional system-maintenance agents in this repository:

- Multi-Agent Workflow Coordinator
- SEO Site Architecture Planner
- Navigation and Mega Menu Architect
- Content Cluster Planner
- Homepage Authority Hub
- Orphan Link Auditor
- Product Knowledge Base Agent
- Product Lifecycle Manager
- Application Page System Agent
- Google SEO and E-E-A-T Content Agent
- AI Product Page Generator Agent
- Standard Relation Auditor
- Internal Linking Architect
- WordPress CPT / ACF Builder
- WordPress Draft Publisher
- Product Publish QA Agent
- Asset Library Manager
- Content Refresh Auditor
- Inquiry Conversion Agent
- Data Import / Export Agent

The Master Agent should coordinate the work and summarize results before any major action.

## Review Requirements

Before any page or function is considered ready, check content accuracy, SEO title and meta description, product data source, source ownership classification, medical and regulatory claim risk, internal links, mobile layout, desktop layout, inquiry CTA, images and alt text, PDF download links, duplicate content risk, security risk, and competitor copying or unsupported claim risk.

## Launch Rules

Before launch, confirm staging site tested, backup completed, inquiry form tested, email delivery tested, mobile pages checked, sitemap generated, robots.txt checked, important pages reviewed, source records reviewed, and final approval received.

Production launch requires manual approval.
