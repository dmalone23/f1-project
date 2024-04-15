from math import sqrt, sin, cos, tan, asin, atan, radians

a = 6378137.0
f = 1 / 298.257223563
b = (1 - f) * a  # radius at the poles, or 6356752.314245


# fmt: off
def calc_sin_σ(U1, U2, λ):
    return sqrt(((cos(U2) * sin(λ)) ** 2)
             + ((cos(U1) * sin(U2) - sin(U1) * cos(U2) * cos(λ)) ** 2))


def calc_cos_σ(U1, U2, λ):
    return sin(U1) * sin(U2) + cos(U1) * cos(U2) * cos(λ)


def calc_sin_α(U1, U2, λ, sin_σ):
    return (cos(U1) * cos(U2) * sin(λ)) / sin_σ


def calc_cos2_α(sin_α):
    return 1 - (sin_α**2)


def calc_cos_2σm(U1, U2, cos_σ, cos2_α):
    return cos_σ - ((2 * sin(U1) * sin(U2)) / cos2_α)


def calc_C(cos2_α):
    return (f / 16) * cos2_α * (4 + (f * (4 - (3 * cos2_α))))


def calc_λ(L, C, sin_α, σ, sin_σ, cos_σ, cos_2σm):
    return L + (1 - C) * f * sin_α * \
            (σ + C * sin_σ * \
             (cos_2σm + C * cos_σ * (-1 + 2 * (cos_2σm**2))))


def calc_u2(α):
    cos2_α = cos(α) ** 2
    return cos2_α * (a**2 - b**2) / b**2


def calc_A(u2):
    return 1 + (u2 / 16384) * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))


def calc_B(u2):
    return (u2 / 1024) * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))


def calc_delta_σ(B, σ, cos_2σm):
    return B * sin(σ) \
            * (cos_2σm + 0.25 * B \
             * (cos(σ) * (-1 + 2 * (cos_2σm**2))
                - (B / 6) * cos_2σm * (-3 + 4 * (sin(σ) ** 2)) * (-3 + 4 * cos_2σm)))


def calc_s(A, σ, delta_σ):
    return b * A * (σ - delta_σ)

# fmt: on
def vincenty(Φ1, L1, Φ2, L2):
    """
    Calculate the distance between two points using Vicenty's inverse formula.
    See here for more: https://en.wikipedia.org/wiki/Vincenty%27s_formulae#Inverse_problem

    Args:
        Φ1: latitude of the first point
        L1: longitude of the first point
        Φ2: latitude of the second point
        L2: longitude of the second point

    Returns:
        s:  ellipsoidal distance between the two points

    Note:
        α1 and α2 (azimuths) are not returned
    """
    lat1 = radians(Φ1)
    long1 = radians(L1)
    lat2 = radians(Φ2)
    long2 = radians(L2)
    U1 = atan((1 - f) * tan(lat1))
    U2 = atan((1 - f) * tan(lat2))
    L = abs(long2 - long1)
    λ = L
    α = 0
    σ = 0
    cos_2σm = 0
    not_converged = True

    while not_converged:
        λ_old = λ

        sin_σ = calc_sin_σ(U1, U2, λ)
        cos_σ = calc_cos_σ(U1, U2, λ)
        σ = asin(sin_σ)
        sin_α = calc_sin_α(U1, U2, λ, sin_σ)
        cos2_α = calc_cos2_α(sin_α)
        α = asin(sin_α)
        cos_2σm = calc_cos_2σm(U1, U2, cos_σ, cos2_α)
        C = calc_C(cos2_α)
        λ = calc_λ(L, C, sin_α, σ, sin_σ, cos_σ, cos_2σm)

        if abs(λ - λ_old) < 1e-12:
            not_converged = False

    u2 = calc_u2(α)
    A = calc_A(u2)
    B = calc_B(u2)
    delta_σ = calc_delta_σ(B, σ, cos_2σm)
    s = calc_s(A, σ, delta_σ)
    print(f"Distance between ({Φ1},{L1}) and ({Φ2},{L2}): {s/1000}\n")
