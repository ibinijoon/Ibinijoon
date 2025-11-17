import numpy as np
import matplotlib.pyplot as plt

# 기본 설정
length = 200       # 거리 (x축) [m]
depth = 20         # 초기 수심 [m]
dx = 1             # 공간 해상도
steps = 50         # 시간 단계 수

# 모델 격자
x = np.arange(0, length, dx)
basement = -depth * np.ones_like(x)              # 고정된 해저면
delta = np.zeros_like(x, dtype=float)            # 실수형 델타 퇴적층

# 퇴적 설정
progradation_rate = 1.0    # 델타 전진 속도 (m/step)
thickness_per_step = 0.5   # 매 단계당 퇴적 두께 (m)

# 시뮬레이션
plt.figure(figsize=(10, 6))
for step in range(steps):
    shoreline = int(progradation_rate * step / dx)
    delta[:shoreline] += thickness_per_step  # 퇴적 진행

    if step % 10 == 0 or step == steps - 1:
        total_surface = basement + delta
        plt.plot(x, total_surface, label=f'Step {step}')

plt.title("2D Delta Progradation Simulation")
plt.xlabel("Distance (m)")
plt.ylabel("Elevation (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

