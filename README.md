# 🦜 `LangChain` LEARNATHON 해커톤 1회 : 1팀 프로젝트
> [!NOTE]
> 1팀 프로젝트 :: MCP(Model Context Protocol) 기반 코드저장소 분석과 질의응답을 자동화하는 멀티 에이전트 시스템

## <img src="https://github.com/user-attachments/assets/00d2c1e4-6970-47e8-9904-712e4a4a3c33" width="30px" height="30px"> 랭체인 러너톤
> 러너톤의 공식 마지막 행사인 해커톤은 AI 기술과 백엔드 아키텍처를 접목해, 실제 서비스 환경에서 바로 적용할 수 있는 프로토타입을 하루 만에 완성해 보는 실무형 해커톤입니다.

### 📅 일정 정보
- 일시: 2025년 3월 29일(토) 오전 9시 ~ 오후 6시
- 장소: 캐럿글로벌 교육센터 2층 (서울특별시 용산구 - 한남동 이태원로 268-20)

### 🌨️ 프로젝트 기간
-  2025년 3월 29일 (토) 하루

## 👼 팀원 소개
|  [장현호](https://github.com/hyunolike)|  장현호 외 4명  |  
| :----------: |  :--------:  
| <img src="https://avatars.githubusercontent.com/hyunolike" width=100px alt="장현호"/>| <img src="https://github.com/user-attachments/assets/57cec2e0-c260-490d-9dc3-0bcaf0bc666a" width=100px alt="이외 4명"/>  | 

<!--
## 🤖 프로젝트 소개
-->


## 1팀 프로젝트 소개
여러분, 이런 경험 한 번쯤 있으시죠? 🤔

"아, 이 프로젝트의 인증 로직은 어디에 있더라..."

"이 함수가 정확히 어떤 역할을 하는 건지 이해하기 어려워..."

새 프로젝트 코드를 뒤적거리며 찾아 헤매던 그 순간들 말이에요.

그럴 때마다 '코드를 쉽게 이해하고 질문할 수 있는 방법 없을까?' 하고 고민하셨다면, 여기 「MCP 기반 코드저장소 분석과 질의응답을 자동화하는 멀티 에이전트 시스템⚡️」 가 있습니다!


#### 이런 분들에게 딱이에요 🙌
- 코드 베이스를 빠르게 이해하고 탐색하고 싶은 분
- 프로젝트 코드에 관한 질문을 실시간으로 해결하고 싶은 분
- 복잡한 코드베이스에서 필요한 정보를 효율적으로 찾고 싶은 분

#### 어떻게 사용하냐고요? 아주 간단해요 🔥
1. 깃허브 레포지토리 URL만 입력하면 자동으로 코드 분석!
2. 자연어로 질문하면 AI가 코드에서 정확한 답변을 찾아줌!
3. 복잡한 코드도 한눈에 이해할 수 있는 직관적인 답변!

<br>

상상해 보세요!

"이 프로젝트에서 인증 로직은 어떻게 구현되어 있지?"라고 물었을 때, 즉시 관련 파일과 함수를 찾아 정확한 설명과 함께 제공합니다.
<br>
저희 또한 개발자로서, 실제 개발자들의 고민을 바탕으로 이 서비스를 만들었어요.
그 경험으로 탄생한 MCP는 개발자의, 개발자에 의한, 개발자를 위한 서비스!

복잡한 설정은 NO! 레포지토리만 연결하면 AI가 자동으로 분석하고, 누구나 자연어로 질문할 수 있는 간편한 UI로 여러분의 코딩 라이프를 업그레이드해 드립니다.
<br>

"코드 이해하느라 고생했던 날은 이제 안녕!"
MCP 기반 코드저장소 분석과 질의응답을 자동화하는 멀티 에이전트 시스템과 함께라면, 새 프로젝트 적응 시간은 번개처럼 빨라질 겁니다. 코드를 분석하고 이해하는 과정이 더 이상 지루하고 번거롭지 않아요.

#### 여러분의 개발 인생에 zap⚡️! 당신의 질문에 코드가 답합니다! 🕺🏻💃🏻
코드를 검색하고 이해하는 시간을 줄이고, 실제 개발에 집중하세요. 여러분의 코드 어시스턴트가 되어 드립니다!
<br>
### 기획 배경

- 새로운 프로젝트나 코드베이스를 접할 때마다 이해하는 데 많은 시간이 소요된다.
- 코드 관련 질문에 대한 답을 찾기 위해 여러 파일을 뒤적거리는 것은 비효율적이다.

### 서비스 주요 기능

- MCP 서버를 통한 코드 저장소 자동 분석
- 임베딩 에이전트로 코드의 구조와 의미를 벡터화
- QA 에이전트로 자연어 질의에 대한 정확한 답변 제공

## 프로젝트 구조
![image](https://github.com/user-attachments/assets/3c25cbf3-44ed-4647-aa0c-d5a0317a0adc)

### 사용자 시나리오
1. 첫 단계: 사용자가 GitHub 저장소 URL 입력
  - 입력: "https://github.com/openai/openai-python 코드를 분석해주세요"
  - 시스템: repo_to_rag 도구가 저장소를 클론하고 분석한 후 기본 정보 제공
  - 응답: "## 저장소 분석 결과 ### 기본 정보 - 저장소 URL: https://github.com/openai/openai-python ..."

2. 두 번째 단계: 사용자가 분석된 코드에 대해 질문
  - 입력: "이 라이브러리에서 API 호출은 어떻게 처리하나요?"
  - 시스템: rag_to_context 도구가 관련 코드 조각을 검색하여 반환
  - 응답: "## Search Results ### Result 1 [코드 조각] Source: openai/api_resources/..."

## Agnet 설명
### [1] 임베딩 에이전트
![image](https://github.com/user-attachments/assets/33a47e60-457f-44f0-9fe7-4d1c9bc7a640)

### [2] QA 에이전트
![image](https://github.com/user-attachments/assets/71b7dc14-e3b6-4c5c-b675-d456864bf4bd)

## 데모
> [!NOTE]
> Cursor AI 사용.


|step 1. 사용자가 Github 저장소 URL 입력|step 2. 사용자가 분석된 코드에 대해 질문|
|:-:|:-:|
|<img width="567" alt="커서AI 데모1" src="https://github.com/user-attachments/assets/ee91a87b-6ec0-42d8-92ea-5b88f940cac6" />|<img width="721" alt="커서AI 데모2" src="https://github.com/user-attachments/assets/12688ab8-86f0-4c37-a1e9-1a2644e367c2" />|

---
### 테스트 자료
|테스트 명|바로 가기|
|-|-|
|MCP Server 이용해 MCP Host 동작 테스트 (RAG 시스템)|[mcp-test](https://github.com/codepresso-learnathon-1st/mcp-test/tree/27740d6a9c1985678e9f4bd265c52bc131daa0bc)|





