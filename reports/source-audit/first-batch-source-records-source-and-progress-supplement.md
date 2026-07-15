# 第一批 Source Record 来源分级与内部进展补充

## 适用范围

本文件是 `reports/source-audit/first-batch-source-records.md` 的补充记录，用于增加资料来源分级和内部进展确认字段。

不推翻原 Source Record，不把第一阶段 20 个方向改成成熟现货产品，不公开老板未确认的内部进展。

## 资料来源分级

- P0: KingPo 已有官网 / PDF / 图片 / 内部确认资料
- P1: 官方标准 / 标准映射资料
- P2: 用户后续补充资料
- P3: 同行参考，仅用于结构学习和测试项目理解，不作为 KingPo 产品事实来源

## 默认内部进展字段

除非老板后续明确确认，每个方向默认使用以下字段：

- Internal Progress Status: Pending boss confirmation / 可能已有内部进展，待老板确认。
- Boss Confirmation Status: Pending / 待老板确认。
- Public Disclosure Permission: Not approved yet / 暂未批准公开。
- Prototype Evidence: Not provided yet / 尚未提供证据。
- Can Mention Internal Progress Publicly: No / 暂不公开提及内部进展。

## 20 个方向补充状态表

| # | Product Direction | Source Priority Layer | Internal Progress Status | Boss Confirmation Status | Public Disclosure Permission | Prototype Evidence | Can Mention Internal Progress Publicly | Notes for Boss Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 脑机接口测试设备 | P0 背景能力 + P1 标准映射 + P2 待补 + P3 结构学习 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认是否已有 BCI 方案、系统图、信号链路、样机或可公开研发描述 |
| 2 | 有源植入式医疗器械测试设备 | P0 背景能力 + P1 ISO 14708/GB/YY 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认 AIMD 具体模块、ISO 14708 适用范围、是否可作为分类页公开 |
| 3 | 电生理动态模拟闭环测试仪 | P0 ECG/电极背景 + P1 闭环标准映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认闭环架构、信号类型、软件逻辑、是否有样机或模块 |
| 4 | EEG 动态模拟闭环测试仪 | P0 生理信号/ECG 背景 + P1 IEC 60601-2-26 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认 EEG 通道、波形、闭环响应、是否可先做样板页草稿 |
| 5 | 头部植入器械综合应力模拟测试仪 | P0 医疗测试设备背景 + P1 ISO/ASTM 待映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认样品对象、机械应力项目、夹具/系统图、是否可公开 |
| 6 | 经皮能量传递测试仪 | P0 医疗电气背景 + P1 ISO/IEC 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认供能架构、功率/频率/温升、EMC 边界和可公开程度 |
| 7 | 植入式医疗器械除颤兼容测试仪 | P0 除颤电极背景 + P1 IEC 60601-2-4 / ISO 14708 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 高优先级确认：是否已有方案、波形/能量、安全边界、是否暂不公开 |
| 8 | 大功率电场模拟器 | P0 医疗电气背景 + P1 EMC 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 高优先级确认：场强、频段、屏蔽、安全联锁、公开风险 |
| 9 | 超声兼容测试仪 | P0 医疗测试设备背景 + P1 IEC 60601-2-37 背景映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认超声源、测试对象、参数、是否与 BCI/AIMD 相关 |
| 10 | 有源植入式器械机械应力综合测试套件 | P0 医疗测试设备背景 + P1 ISO/ASTM 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认机械模块清单、夹具、载荷、循环条件、图片 |
| 11 | 压力循环测试系统 | P0 医疗测试设备背景 + P1 标准映射待确认 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认压力范围、介质、样品对象、循环次数和系统图 |
| 12 | 电极耐压自动测试仪 | P0 ECG/电极/医疗电气背景 + P1 IEC 60601-1 / ISO 14708 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 高优先级确认：电极类型、耐压条件、夹具、自动化程度、可做样板页否 |
| 13 | 静磁场测试系统 | P0 医疗电气背景 + P1 磁场/MRI 背景映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认磁场强度、磁源、样品对象、是否涉及 MRI 安全风险 |
| 14 | 时变磁场测试仪 | P0 EMC/医疗电气背景 + P1 IEC 61000-4-8 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认频率、波形、线圈、暴露条件和标准适用性 |
| 15 | 心律管理器械低频电磁抗扰度测试仪 | P0 ECG/除颤/医疗电气背景 + P1 ISO 14708-2 / EMC 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 高优先级确认：起搏器/ICD 对象、抗扰度条件、监测方法、是否暂不公开 |
| 16 | 多通道光纤检测仪 | P0 医疗测试设备背景 + P1 数据接口/安全背景 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认医疗用途、通道数、波长、接口和是否与 BCI/AIMD 关联 |
| 17 | 神经刺激器电极组织接口网络模块 | P0 电极/医疗电气背景 + P1 ISO 14708-3 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 高优先级确认：等效网络、组织模型、神经刺激器对象、可公开程度 |
| 18 | IPG 注入测试系统 | P0 植入式/医疗电气背景 + P1 ISO 14708 映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 高优先级确认：“注入”定义、IPG 类型、测试对象、电气参数 |
| 19 | 植入器械 TMS 兼容性测试仪 | P0 医疗电气/EMC 背景 + P1 TMS/磁场标准待确认 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 高优先级确认：TMS 暴露条件、风险边界、是否可公开、标准适用性 |
| 20 | 超声脑机接口性能测试仪 | P0 医疗测试设备背景 + P1 超声标准背景映射 + P2 待补 | Pending boss confirmation / 可能已有内部进展，待老板确认 | Pending / 待老板确认 | Not approved yet / 暂未批准公开 | Not provided yet / 尚未提供证据 | No / 暂不公开提及内部进展 | 确认超声 BCI 技术路线、性能指标、超声参数、是否已有方案 |

## 老板优先确认方向

1. 植入式医疗器械除颤兼容测试仪
2. 心律管理器械低频电磁抗扰度测试仪
3. 植入器械 TMS 兼容性测试仪
4. 电极耐压自动测试仪
5. 神经刺激器电极组织接口网络模块
6. IPG 注入测试系统
7. 脑机接口测试设备
8. 有源植入式医疗器械测试设备

## 老板确认后最适合先做样板页的方向

1. 脑机接口测试设备
2. 有源植入式医疗器械测试设备
3. EEG 动态模拟闭环测试仪
4. 电生理动态模拟闭环测试仪
5. 电极耐压自动测试仪
6. 神经刺激器电极组织接口网络模块

## 老板最小确认问题清单

每个方向只需要老板先回答以下最小问题即可推进草稿：

1. 该方向是否可以公开提及？
2. 当前状态是研发中、技术预研、可定制开发评估，还是暂不公开？
3. 是否已有方案、模块、样机、测试夹具、系统图或 PDF？
4. 是否允许公开“已有内部进展”？
5. 可以公开哪些图片、图纸、PDF 或系统图？
6. 适用标准、版本和条款方向是否已有内部确认？
7. 哪些参数可以公开，哪些必须写“需要人工确认”？
8. 是否允许进入第一批研发方向页草稿？