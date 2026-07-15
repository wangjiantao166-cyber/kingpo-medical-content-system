---
status: profile
scope: medical-cn
do_not_route: true
superseded_by: docs/00-system-scope-and-sites.md
---

# 国际医疗器械标准体系映射

## 目的

本文件用于为“脑机接口与有源植入式医疗器械测试设备中文站”建立国际医疗器械标准映射体系。

当前阶段只做标准体系规划和映射规则，不生成产品页面，不声明 KingPo 产品已完全符合任何标准。

## 核心规则

- 不得把标准号写成 KingPo 产品已完全符合，除非有明确资料支持。
- 不得编造标准版本、条款号、测试条件或适用范围。
- 每个产品方向必须先做标准映射，再决定是否可以写页面。
- 如果标准适用性不确定，标记为“需要人工确认”，不要写进最终产品页。
- 同行资料只能用于理解测试项目、用户需求和页面结构，不能作为 KingPo 产品参数来源。
- 标准名称、版本、条款和测试条件必须以官方标准、用户提供资料或可核对技术文件为准。

## 标准映射字段

每条标准映射记录必须包含：

- Standard Number
- Standard Name
- Organization
- Relevance to Product Direction
- Test Object
- Possible Test Item
- Page Use: 主标准 / 辅助标准 / 背景标准 / 不适用
- Evidence Source
- Human Verification Required

## 1. IEC 60601 基础与并列标准

| Standard Number | Standard Name | Organization | Relevance to Product Direction | Test Object | Possible Test Item | Page Use | Evidence Source | Human Verification Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IEC 60601-1 | Medical electrical equipment - General requirements for basic safety and essential performance | IEC | 医疗电气安全基础要求；可作为医疗电气安全、患者漏电流、绝缘和保护措施相关页面背景 | 医疗电气设备、相关测试系统 | 基本安全、基本性能、漏电流、绝缘、耐压等方向，具体条款需确认 | 主标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-1-2 | EMC collateral standard | IEC | 医疗电气设备 EMC 抗扰度和发射相关方向 | 医疗电气设备、测试系统 | ESD、RF、电快速瞬变、浪涌、传导抗扰、工频磁场等方向，具体条件需确认 | 主标准 / 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-1-6 / IEC 62366-1 | Usability engineering collateral / usability engineering for medical devices | IEC | 人因工程、可用性、使用风险相关页面背景 | 医疗设备、软件界面、操作流程 | 可用性工程、用户操作风险；通常不是设备参数来源 | 背景标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-1-8 | Alarm systems collateral standard | IEC | 报警系统相关设备或监护类页面背景 | 医疗电气设备报警系统 | 报警信号、报警系统要求；仅在产品相关时使用 | 辅助标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-1-10 | Physiologic closed-loop controller collateral standard | IEC | 闭环神经刺激、闭环控制、自动反馈控制相关方向 | 生理闭环控制系统 | 闭环控制安全、控制器行为、风险控制方向，具体条款需确认 | 主标准 / 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-1-11 | Home healthcare environment collateral standard | IEC | 家用医疗环境相关背景，第一阶段通常低优先级 | 家用医疗电气设备 | 家用环境要求；仅在产品定位涉及家庭使用时使用 | 背景标准 / 不适用 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-1-12 | Emergency medical services environment collateral standard | IEC | 急救环境相关背景，第一阶段通常低优先级 | 急救医疗电气设备 | 急救环境要求；仅在产品涉及 EMS 场景时使用 | 背景标准 / 不适用 | 需要官方标准或用户资料确认 | Yes |

## 2. IEC 60601 相关专用标准

| Standard Number | Standard Name | Organization | Relevance to Product Direction | Test Object | Possible Test Item | Page Use | Evidence Source | Human Verification Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IEC 60601-2-26 | Particular requirements for electroencephalographs | IEC | EEG 信号模拟、EEG 动态模拟闭环测试相关 | EEG 设备、EEG 信号链路 | EEG 相关性能、安全和信号方向，具体测试条件需确认 | 主标准 / 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-27 | Particular requirements for electrocardiographic monitoring equipment | IEC | ECG、监护、心电信号相关方向 | ECG 监护设备 | ECG 信号、监护性能、抗干扰方向，具体条件需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-34 | Particular requirements for invasive blood pressure monitoring equipment | IEC | 压力循环、侵入式压力监测相关背景 | 侵入式血压监测设备 | 压力测量相关方向，是否适用需确认 | 辅助标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-47 | Particular requirements for ambulatory electrocardiographic systems | IEC | 动态 ECG、长时程信号测试相关背景 | 动态 ECG 系统 | ECG 信号记录和性能方向，是否适用需确认 | 辅助标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-49 | Particular requirements for multifunction patient monitoring equipment | IEC | 多参数监护、ECG/生理信号相关背景 | 多参数监护设备 | 多参数监护性能方向，是否适用需确认 | 辅助标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-4 | Particular requirements for cardiac defibrillators | IEC | 除颤兼容、除颤电极、ICD 相关方向 | 除颤器、相关接口或电极 | 除颤脉冲、兼容性和安全相关方向，具体条件需确认 | 主标准 / 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-31 | Particular requirements for external cardiac pacemakers with internal power source | IEC | 起搏、心律管理器械相关参考 | 外部心脏起搏器 | 起搏输出、低频电磁抗扰度等方向，是否适用需确认 | 辅助标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-33 | Particular requirements for MRI equipment | IEC | 静磁场、时变磁场、MRI 兼容相关背景 | MRI 设备及相关环境 | 磁场相关场景；用于植入器械磁场兼容时需谨慎映射 | 背景标准 / 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 60601-2-37 | Particular requirements for ultrasonic medical diagnostic and monitoring equipment | IEC | 超声兼容、超声脑机接口性能测试相关背景 | 超声诊断/监护设备 | 超声输出、安全和兼容方向，具体适用需确认 | 辅助标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |

## 3. 有源植入式医疗器械标准

| Standard Number | Standard Name | Organization | Relevance to Product Direction | Test Object | Possible Test Item | Page Use | Evidence Source | Human Verification Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISO 14708 series | Active implantable medical devices series | ISO | 有源植入式医疗器械总体系 | 有源植入式医疗器械 | 通用安全、性能、植入式器械测试方向，具体分部分需确认 | 主标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 14708-1 | Active implantable medical devices - General requirements | ISO | 有源植入式医疗器械通用要求 | 有源植入式医疗器械 | 通用要求、风险、安全、性能方向，具体测试条件需确认 | 主标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 14708-2 | Active implantable medical devices - Cardiac pacemakers | ISO | 起搏器、心律管理相关测试方向 | 植入式起搏器 | 起搏相关安全和性能方向，具体条件需确认 | 主标准 / 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 14708-3 | Active implantable medical devices - Implantable neurostimulators | ISO | 神经刺激器、BCI 相关测试方向 | 植入式神经刺激器 | 刺激输出、植入器械安全和性能方向，具体条件需确认 | 主标准 | 需要官方标准或用户资料确认 | Yes |
| Other ISO 14708 parts | Other active implantable medical device parts | ISO | 仅在产品对象适用且来源确认后使用 | 待确认 | 待确认 | 辅助标准 / 不适用 | 需要官方标准或用户资料确认 | Yes |

## 4. 医疗器械通用标准

| Standard Number | Standard Name | Organization | Relevance to Product Direction | Test Object | Possible Test Item | Page Use | Evidence Source | Human Verification Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISO 10993 series | Biological evaluation of medical devices | ISO | 生物学评价背景；通常不是测试设备参数来源 | 医疗器械材料/接触部件 | 生物相容性评价方向；产品页慎用 | 背景标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 14971 | Application of risk management to medical devices | ISO | 风险管理背景 | 医疗器械和测试方案 | 风险管理、危害分析背景 | 背景标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 13485 | Quality management systems for medical devices | ISO | 质量体系背景，不作为产品测试参数来源 | 医疗器械组织/质量体系 | 质量体系要求 | 背景标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 14155 | Clinical investigation of medical devices | ISO | 临床研究背景，不作为设备参数来源 | 临床研究 | 临床评价/研究背景，页面慎用 | 背景标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 15223-1 | Symbols to be used with medical device labels | ISO | 标签符号背景 | 医疗器械标签 | 标识符号，不作为测试设备参数来源 | 背景标准 | 需要官方标准或用户资料确认 | Yes |
| ISO 20417 | Information to be supplied by the manufacturer | ISO | 制造商提供信息背景 | 医疗器械随附信息 | 标签、说明书和信息提供背景 | 背景标准 | 需要官方标准或用户资料确认 | Yes |

## 5. EMC / 磁场 / TMS / 抗扰度相关标准

| Standard Number | Standard Name | Organization | Relevance to Product Direction | Test Object | Possible Test Item | Page Use | Evidence Source | Human Verification Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IEC 60601-1-2 | EMC requirements and tests for medical electrical equipment | IEC | 医疗 EMC 主线标准 | 医疗电气设备 | 抗扰度和发射测试方向，具体条件需确认 | 主标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 61000-4-2 | Electrostatic discharge immunity test | IEC | ESD 抗扰度方向 | 设备端口、外壳、接口 | 静电放电抗扰度，具体等级需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 61000-4-3 | Radiated RF electromagnetic field immunity test | IEC | 射频电磁场抗扰度方向 | 医疗电气设备 | 辐射 RF 抗扰度，具体条件需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 61000-4-4 | Electrical fast transient/burst immunity test | IEC | 电快速瞬变抗扰度方向 | 电源/信号端口 | EFT/Burst 抗扰度，具体条件需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 61000-4-5 | Surge immunity test | IEC | 浪涌抗扰度方向 | 电源/信号端口 | Surge 抗扰度，具体条件需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 61000-4-6 | Conducted disturbances induced by RF fields immunity test | IEC | 传导射频抗扰度方向 | 电源/信号端口 | 传导 RF 抗扰度，具体条件需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 61000-4-8 | Power frequency magnetic field immunity test | IEC | 低频磁场抗扰度方向 | 医疗电气设备、心律管理相关测试 | 工频磁场抗扰度，具体条件需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| IEC 61000-4-39 | Radiated fields in close proximity immunity test | IEC | 近场抗扰度方向；仅在适用且来源确认后使用 | 医疗电气设备近场环境 | 近场抗扰度，适用性需确认 | 辅助标准 / 不适用 | 需要官方标准或用户资料确认 | Yes |

## 6. ANSI / AAMI / ASTM / IEEE 参考标准

| Standard Number | Standard Name | Organization | Relevance to Product Direction | Test Object | Possible Test Item | Page Use | Evidence Source | Human Verification Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ANSI/AAMI EC12 | Disposable ECG electrodes | ANSI/AAMI | ECG 电极性能测试方向 | 一次性 ECG 电极 | 电极性能、接触、信号相关方向，具体条件需确认 | 辅助标准 / 主标准 | 需要官方标准或用户资料确认 | Yes |
| ANSI/AAMI EC13 | Cardiac monitors, heart rate meters, and alarms | ANSI/AAMI | ECG 监护和心电信号相关方向 | 心电监护设备 | ECG 监护性能方向，具体条件需确认 | 辅助标准 | 需要官方标准或用户资料确认 | Yes |
| ANSI/AAMI DF80 | Implantable defibrillators | ANSI/AAMI | ICD / 除颤兼容方向；仅在适用且来源确认后使用 | 植入式除颤器 | 除颤相关测试方向，具体条件需确认 | 辅助标准 / 不适用 | 需要官方标准或用户资料确认 | Yes |
| ANSI/AAMI PC69 | Active implantable medical device related reference | ANSI/AAMI | 仅在适用且来源确认后使用 | 待确认 | 待确认 | 辅助标准 / 不适用 | 需要官方标准或用户资料确认 | Yes |
| Relevant AAMI TIR documents | Technical information reports | AAMI | 仅作参考指导，不直接作为产品符合性声明 | 医疗器械研发/风险/测试参考 | 指导性资料 | 背景标准 | 需要官方资料或用户确认 | Yes |
| Relevant ASTM F-series standards | ASTM F-series medical/device material standards | ASTM | 仅在产品对象确认后使用 | 电极、导线、材料、植入相关对象 | 机械、材料、疲劳、兼容等方向，具体标准需确认 | 主标准 / 辅助标准 / 不适用 | 需要官方标准或用户资料确认 | Yes |
| IEEE / ISO/IEEE 11073 | Health informatics / device communication standards | IEEE / ISO / IEEE | 仅用于通信或数据接口相关页面 | 医疗设备通信接口 | 数据接口、通信协议方向，非通用产品参数来源 | 辅助标准 / 背景标准 | 需要官方标准或用户资料确认 | Yes |

## 产品页使用流程

1. 先建立产品方向 source record。
2. 再建立标准映射表。
3. 判断每个标准的 Page Use：主标准 / 辅助标准 / 背景标准 / 不适用。
4. 对标准版本、条款号、测试条件、样品对象进行人工确认。
5. 只有已确认的标准映射才能进入最终产品页。
6. 未确认标准只能保留在内部 source record 或标记为“需要人工确认”。

## 禁止写法

禁止在页面中写：

- 本产品完全符合某标准，除非有明确来源。
- 本产品覆盖某标准全部条款，除非有明确来源。
- 未确认的标准版本、条款号、测试条件。
- 根据同行资料推断出的 KingPo 参数。
- 将背景标准写成主标准。

