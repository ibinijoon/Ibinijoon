import numpy as np
import matplotlib.pyplot as plt

# 모델 공간 설정
length = 200
dx = 1
x = np.arange(0, length, dx)

# 초기 지형 설정
depth = 20
basement = -depth * np.ones_like(x)
delta = np.zeros_like(x, dtype=float)

# 파라미터
steps = 80
thickness_per_step = 1.0  # 퇴적 두께 (조금 더 크게)
progradation_rate = 2.0   # 초기 전진 속도 (빠르게)
retreat_rate = 5.0        # 후퇴 속도 (강하게)
supply_drop_step = 40     # 퇴적물 공급 갑작스런 감소 시점

# 초기 퇴적 공급량
sediment_supply = 1.0

plt.figure(figsize=(12, 6))

for step in range(steps):
    # 퇴적물 공급 급감 시점 넘으면 공급 0으로 만듦
    if step == supply_drop_step:
        sediment_supply = 0.0

    # 전진 거리 계산 (퇴적 공급에 비례)
    effective_progradation = progradation_rate * sediment_supply * step
    shoreline = int(effective_progradation / dx)

    # 퇴적: 전진 중인 구간에 퇴적 두께 추가
    if shoreline > 0:
        delta[:shoreline] += thickness_per_step

    # 후퇴 발생: 공급이 0이 되면 후퇴가 강하게 일어남
    if sediment_supply == 0.0 and shoreline > 0:
        retreat_cells = int(retreat_rate / dx)
        retreat_start = max(0, shoreline - retreat_cells)
        delta[retreat_start:shoreline] -= thickness_per_step * 3  # 침식 강도 크게

        # 음수 두께 방지
        delta[delta < 0] = 0

    # 시각화 (10 스텝마다)
    if step % 10 == 0 or step == steps - 1:
        total_surface = basement + delta
        plt.plot(x, total_surface, label=f"Step {step}")

plt.title("Extreme Delta Autoretreat Simulation")
plt.xlabel("Distance (m)")
plt.ylabel("Elevation (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
