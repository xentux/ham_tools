# This script calculates all needed wire length for an linked EndFed HalfWave
# for the following bands:
# 60, 40, 30, 20 17

BANDS = {
    60: 5.35,
    40: 7,
    30: 10.1,
    20: 14,
    17: 18.07

}
VELOCITY_FACTOR = 0.97

halfwaves = {}

print(f"Velocity factor: {VELOCITY_FACTOR}\n")
for band in BANDS:
    wavelength = 300 / BANDS[band]
    halfwave = wavelength / 2 * VELOCITY_FACTOR
    halfwaves[band] = halfwave
    print(f"- {BANDS[band]:>5.1f} MHz: λ = {wavelength:.2f} m - λ/2 = {wavelength/2:.2f} m - wire: {halfwave:.2f} m")

print("\n-----wire A-----|=|---wire B---      |=| : 25 µH with bypass\n")

wire_a = halfwaves[30]
wire_b = halfwaves[40] - halfwaves[30]
#print("\n")
print(f"- wire A: {wire_a:.2f} m")
print(f"- wire B: {wire_b:.2f} m")