"""
Neurons Engine - 기본 사용 예제
Basic Usage Example

이 예제는 Neurons Engine의 기본 사용법을 보여줍니다.
"""

from neurons import CA3Neuron, DGNeuron
import numpy as np

def example_ca3_neuron():
    """CA3 뉴런 기본 사용 예제"""
    print("=== CA3 뉴런 예제 ===")
    
    # CA3 뉴런 생성
    neuron = CA3Neuron(
        neuron_id="CA3_0",
        baseline_V=-65.0,      # 기본 막전위 [mV]
        threshold=-31.5        # 스파이크 임계값 [mV]
    )
    
    print(f"초기 막전위: {neuron.V} mV")
    print(f"임계값: {neuron.threshold} mV")
    
    # 뉴런 업데이트 (0.1ms 시간 스텝)
    for i in range(100):
        # 입력 전류 주입 (10.0 pA)
        I_total = 10.0
        neuron.step(dt=0.1, I_total=I_total)
        
        # 스파이크 발생 확인
        if neuron.spike_count > 0:
            print(f"스텝 {i}: 스파이크 발생! 막전위: {neuron.V:.2f} mV")
            break
    
    print(f"최종 막전위: {neuron.V:.2f} mV")
    print(f"총 스파이크 수: {neuron.spike_count}")
    print()


def example_dg_neuron():
    """DG 뉴런 기본 사용 예제"""
    print("=== DG 뉴런 예제 ===")
    
    # DG 뉴런 생성
    neuron = DGNeuron(
        neuron_id="DG_0",
        baseline_V=-65.0,
        threshold=-31.5
    )
    
    print(f"초기 막전위: {neuron.V} mV")
    
    # 뉴런 업데이트
    for i in range(100):
        I_total = 8.0
        neuron.step(dt=0.1, I_total=I_total)
        
        if neuron.spike_count > 0:
            print(f"스텝 {i}: 스파이크 발생! 막전위: {neuron.V:.2f} mV")
            break
    
    print(f"최종 막전위: {neuron.V:.2f} mV")
    print(f"총 스파이크 수: {neuron.spike_count}")
    print()


if __name__ == "__main__":
    print("Neurons Engine - 기본 사용 예제\n")
    
    # CA3 뉴런 예제
    example_ca3_neuron()
    
    # DG 뉴런 예제
    example_dg_neuron()
    
    print("예제 실행 완료!")

