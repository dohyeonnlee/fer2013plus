![Untitled (3)](https://github.com/westnowise/fer2013plus/assets/98007431/015868e4-15c6-4624-835a-a4d6ad585e70)# 😀fer2013plus😂
![Untitled](https://github.com/westnowise/fer2013plus/assets/98007431/c07aba3a-13de-4c9c-a086-f058884a0aac)

## ⚙️요약
### 주제
비대면 교육 환경에서의 학생들의 학습 상태를 실시간으로 모니터링하고 이해하기 위한 얼굴 표정 인식 분류 모델 개발

표정을 통해 학습 상태를 인식하는 것에 목적을 둠

### 데이터 
FER2013 데이터셋의 오류 개선한 FER+ 데이터셋 사용

### 모델 선정 및 훈련
- VGG16, VGG19, ResNet34, ResNet50 모델을 고려
- 학습률, 옵티마이저 등 다양한 하이퍼파라미터 조정을 통해 여러 훈련 진행
- 데이터 증강 후 모델 재훈련

### 최종 모델 선정
VGG19

## 과정 및 결과
### 기본 모델 결과
- 파라미터 설정
    - Optimizer: SGD+Momentum
    - LR: 0.01
    - ⇒ ResNet보다 VGG의 모델이 더 좋은 성능을 보임
![Untitled (2)](https://github.com/westnowise/fer2013plus/assets/98007431/6c93765d-521b-4e1f-b6a6-ccb4d52b18b0)
![Untitled (1)](https://github.com/westnowise/fer2013plus/assets/98007431/7d55c7c0-2b15-49b4-82ff-e326f8dbdbb0)
![Untitled (3)](https://github.com/westnowise/fer2013plus/assets/98007431/4bcae06d-1bce-4a2b-9ad4-9522cf86dfca)


### 하이퍼 파라미터 조정
    - Optimizer: SGD+Momentum → Adam
    - Dropout
    - Learning rate: 0.01 → 0.001, 0.1
    - ⇒ lr=0.001의 그래프 결과가 가장 좋았으나, epoch 늘린 후 과적합 형태를 보임
![Untitled (1)](https://github.com/westnowise/fer2013plus/assets/98007431/8b15b045-01e8-4fd6-827e-56270582aa00)
![Untitled (5)](https://github.com/westnowise/fer2013plus/assets/98007431/8ac04cfb-351c-40ff-884d-1fc69c0acb44)
![Untitled (3)](https://github.com/westnowise/fer2013plus/assets/98007431/0c887cb8-9775-491d-96ce-f0ed171ab871)


### 데이터 증강
- 기존 데이터에서 filp, rotate 한 데이터를 병합하여 35,886개 → 107,315개로 증강
- 증강 전 데이터에서 성능이 가장 높았던 VGG19 모델 채택하여 증강 후 데이터에 VGG19 모델로 재훈련
- ⇒ Accuracy 기준 가장 좋은 성능을 보임
![Untitled (1)](https://github.com/westnowise/fer2013plus/assets/98007431/8cf98a08-fde7-41c7-a18c-a266624b8106)
![Untitled (2)](https://github.com/westnowise/fer2013plus/assets/98007431/2c5fee90-cc7b-4f77-93c5-2bcef674c88c)
![Untitled (3)](https://github.com/westnowise/fer2013plus/assets/98007431/34eebb9e-4d1a-488e-ac96-0eccfbb9fbac)
![Untitled](https://github.com/westnowise/fer2013plus/assets/98007431/8702ec29-7e78-4cdf-b7b0-bd227eb3b37e)


### 최종 모델 선정
- Accuracy, Loss, 그래프 모양을 모두 종합하여 판단
  ⇒ **VGG19의 기본 파라미터(SGD+Momentum, lr=0.01) 모델 선정**
![Untitled (4)](https://github.com/westnowise/fer2013plus/assets/98007431/110b28ab-c56e-4962-b246-b5e6900fcbfd)

- FER2013 데이터를 이용한 모델 지표 리더보드 비교
![Untitled (5)](https://github.com/westnowise/fer2013plus/assets/98007431/9c998829-35a9-4a92-bb8e-14f23414aae5)

### 시연
![Untitled (6)](https://github.com/westnowise/fer2013plus/assets/98007431/7506e56d-952e-4df3-b9b5-6fe0752a2f39)


## ⚒️ 개발 환경 / Tool ⚒️
- Python
- Pandas, Numpy, Pytorch, Matplotlib, OpenCV, Gradio
- Jupyter Notebook, VS Code


## 기간
2024.04.03.~2024.04.05, 총 5일

## 멤버 
|               | github                             | R&R |
| ------------- | ---------------------------------- | -------|
| 윤소현 |    | 팀장, 모델 훈련, 그라디오, PPT  |
| 송희도      | |     개발 환경 세팅, 모델 훈련, 성능 확인, PPT   |
| 이도현  |    |모델 훈련, 파라미터 수정, 발표, PPT|
| 조서현      |   https://github.com/westnowise      |이미지 전처리, 모델 훈련, 성능 확인, PPT|
