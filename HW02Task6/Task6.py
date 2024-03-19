def main():
    M1 = float(input("M1 (kg): "))
    M2 = float(input("M2 (kg): "))
    M3 = float(input("M3 (kg): "))

    u1 = float(input("Velocity of M1 (m/s): "))
    u2 = float(input("Velocity of M2 (m/s): "))
    u3 = float(input("Velocity of M3 (m/s): "))

    L = float(input("Rope length (m): "))
    dt = float(input("Time step (s): "))
    D_max = 0
    position1 = 0
    a1 = 0
    a2 = 0
    a3 = 0

    while True:
        a1 = (M2 * u2 * u2 - M3 * u3 * u3) / (M1 + M2 + M3)
        a2 = (u1 * u1 - u3 * u3) / L
        a3 = (2 * M2 * u2 * u2 - M1 * u1 * u1) / (M1 + M2 + M3)

        u1 += a1 * dt
        u2 += a2 * dt
        u3 += a3 * dt

        position1 += u1 * dt
        D_max = position1 if position1 > D_max else D_max

        if u3 <= 0: break


    print("Maximal distance moved: {:.2f} m".format(D_max))

if __name__ == "__main__":
    main()
