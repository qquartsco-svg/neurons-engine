# Neurons Engine

**뉴런 엔진 - 신경망의 기본 구성 요소**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/qquartsco-svg/neurons-engine)
[![Status](https://img.shields.io/badge/status-commercial%20ready-green.svg)](https://github.com/qquartsco-svg/neurons-engine)

**English**: [README_EN.md](README_EN.md)

---

## 🎯 무엇을 하는가

**Neurons Engine**은 신경망의 기본 구성 요소인 뉴런 모델을 제공하는 엔진입니다.

**핵심 구성 요소**:
- `CA3Neuron` - 해마 CA3 영역 뉴런 모델
- `DGNeuron` - 치아이랑(Dentate Gyrus) 뉴런 모델
- `SpatialNeuron` - 공간 뉴런 모델

**용도**:
- 신경망 연구
- 생물학적 신경 모델링
- 인공지능 연구
- 패턴 완성 및 분리

---

## 🚀 빠른 시작

### 설치

```bash
pip install -r requirements.txt
```

또는 개발 모드로 설치:

```bash
pip install -e .
```

### 기본 사용법

```python
from neurons import CA3Neuron

# CA3 뉴런 생성
neuron = CA3Neuron(
    neuron_id="CA3_0",
    baseline_V=-65.0,      # 기본 막전위 [mV]
    threshold=-31.5        # 스파이크 임계값 [mV]
)

# 뉴런 업데이트 (0.1ms 시간 스텝)
neuron.step(dt=0.1, I_total=10.0)  # I_total: 총 입력 전류 [pA]

# 스파이크 발생 여부 확인
if neuron.spike_count > 0:
    print(f"스파이크 발생! 현재 막전위: {neuron.V} mV")
```

---

## 📁 프로젝트 구조

```
neurons-engine/
├── neurons/                    # 뉴런 모델 패키지
│   ├── __init__.py            # 패키지 초기화
│   ├── neurons.py             # CA3, DG 뉴런 모델
│   └── spatial_neurons.py     # 공간 뉴런 모델
├── tests/                      # 테스트 스위트
│   └── test_neurons.py        # 뉴런 테스트
├── examples/                   # 사용 예제
│   └── basic_usage.py         # 기본 사용 예제
├── docs/                       # 기술 문서
├── README.md                   # 이 파일 (한국어 - 메인)
├── README_EN.md                # 영어 버전
├── LICENSE                     # MIT 라이선스
├── setup.py                    # 패키지 설정
├── requirements.txt            # 의존성
├── BLOCKCHAIN_HASH_RECORD.md   # 블록체인 해시 기록
├── GPG_SIGNING_GUIDE.md        # GPG 서명 가이드
├── REVENUE_SHARING.md          # 코드 재사용 수익 분배 원칙
└── CHANGELOG.md                # 변경 이력
```

---

## 🔬 기술 배경

### CA3 뉴런
- **생물학적 기반**: 해마 CA3 영역
- **특징**: 
  - STDP 학습 (Spike-Timing Dependent Plasticity)
  - Homeostasis 메커니즘
  - Recurrent connections
- **용도**: 패턴 완성, 상태 유지

### DG 뉴런
- **생물학적 기반**: 치아이랑(Dentate Gyrus)
- **특징**: 
  - 패턴 분리 (Pattern Separation)
  - 희소 표현 (Sparse Representation)
- **용도**: 입력 전처리

### Spatial 뉴런
- **특징**: 공간 정보 처리
- **용도**: 공간 인식, 위치 추적

---

## 📚 문서

### 사용 가이드
- `README.md` (한국어 - 메인)
- `README_EN.md` (영어)

### 기술 문서
- `docs/` - 상세 기술 문서

### 예제
- `examples/` - 사용 예제 코드

---

## 🧪 테스트

### 모든 테스트 실행
```bash
pytest tests/ -v
```

### 특정 테스트 실행
```bash
pytest tests/test_neurons.py -v
```

---

## 💰 코드 재사용 수익 분배

코드 재사용으로 수익이 발생할 경우 분배 원칙은 `REVENUE_SHARING.md`를 참조하세요.

---

## 🔐 블록체인 해시 기록

이 프로젝트는 블록체인 해시 기록을 사용하여:
- 공개 발매 증명
- 파일 무결성 보장
- 기술적 선행 기술 증명

**해시 기록**: `BLOCKCHAIN_HASH_RECORD.md` 참조

---

## 📝 라이선스

**MIT 라이선스** - 자세한 내용은 `LICENSE` 파일 참조

이 기술은 공개적으로 사용 가능하며 (특허 없음) 다음과 같이 사용할 수 있습니다:
- 연구/교육용 자유 사용
- 상업적 사용시 `REVENUE_SHARING.md` 참조

---

## 🎯 응용 분야

- 신경망 연구
- 생물학적 신경 모델링
- 인공지능 연구
- 패턴 완성 및 분리
- 공간 인식

---

## 📞 문의

**GitHub Issues**: [레포지토리 Issues](https://github.com/qquartsco-svg/neurons-engine/issues)

---

## 🔗 관련 레포지토리

- [ring-attractor-engine](https://github.com/qquartsco-svg/ring-attractor-engine) - 링어트랙트 엔진 (이 뉴런 엔진 사용)

---

**Last Updated**: 2026-01-17  
**Version**: v1.0.0  
**Status**: 상용화 준비 완료 ✅
