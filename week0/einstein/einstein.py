"""A program that outputs the energy equivalent (in J)
   of input mass (in Kg).

   The speed of light is set to SPEED_OF_LIGHT, see Code.
   This program assumes that the user will input an integer."""


SPEED_OF_LIGHT = int(3e8)


def main():
    """Input mass and output energy equivalent."""

    mass = int(input("mass (in kg): ").strip())
    output_energy = get_energy_equivalent(mass, SPEED_OF_LIGHT)

    print("The output energy is: ",
          output_energy,
          sep="\n")


def get_energy_equivalent(mass, speed_of_light):
    """Get the energy equivalent of the given mass."""
    energy = mass * (speed_of_light ** 2)
    return energy


if __name__ == "__main__":
    main()
