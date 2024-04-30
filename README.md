# 😀fer2013plus😂
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
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/97a160f8-79b4-4904-b833-791bbc82aad9)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/62cf3f9a-38c4-4314-bf4e-efebde63f8a3/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/655e34cb-e349-4aad-83df-afeb19fdbf09/Untitled.png)

### 하이퍼 파라미터 조정
    - Optimizer: SGD+Momentum → Adam
    - Dropout
    - Learning rate: 0.01 → 0.001, 0.1
    - ⇒ lr=0.001의 그래프 결과가 가장 좋았으나, epoch 늘린 후 과적합 형태를 보임
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/0213c40e-d309-4795-a0e3-ab2bb36a65ff/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/c935a316-a499-450f-9a46-cd6950cd293b/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/1b065b74-3369-4880-857e-ef0d03dee18d/Untitled.png)

### 데이터 증강
- 기존 데이터에서 filp, rotate 한 데이터를 병합하여 35,886개 → 107,315개로 증강
- 증강 전 데이터에서 성능이 가장 높았던 VGG19 모델 채택하여 증강 후 데이터에 VGG19 모델로 재훈련
- ⇒ Accuracy 기준 가장 좋은 성능을 보임
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/63f9106a-b12e-4a11-9113-88ed1d2887ce/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/43482a58-efab-43ad-a9cf-9f76033e89f5/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/75236e4e-9e8d-40a0-9ef4-4cdc3d939c62/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/2af939fb-b1f7-4a12-a39a-2a29d25960be/Untitled.png)

### 최종 모델 선정
- Accuracy, Loss, 그래프 모양을 모두 종합하여 판단
  ⇒ **VGG19의 기본 파라미터(SGD+Momentum, lr=0.01) 모델 선정**
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/327fed9e-de53-4540-aa2a-296b5b89c41d/Untitled.png)
- FER2013 데이터를 이용한 모델 지표 리더보드 비교
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/29dea121-889c-4678-baaa-246c79f802f0/Untitled.png)

### 시연
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/97fb822e-b52f-496f-9213-da9a8b169502/991cda00-d013-488a-9f42-622bbfb0bc6a/Untitled.png)

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
