"""Manage bitwise patient-data permissions."""


# Step 1: Permissions are like light switches: Read, Write, Delete. We flip switches on or off, and we can ask “is this switch on?”
class PatientPermissions:
    # Step 2: represent each permission as a distinct bit flag
    READ = 1
    WRITE = 2
    DELETE = 4
    ALL = READ | WRITE | DELETE

    def __init__(self, permissions: int = 0):
        # Step 3: store current permissions as one integer
        self.permissions = permissions

    def add_permission(self, permission: int) -> None:
        # Step 4: grant a permission by turning its bit on
        self.permissions |= permission

    def remove_permission(self, permission: int) -> None:
        # Step 5: revoke a permission by turning its bit off
        self.permissions &= ~permission

    def has_permission(self, permission: int) -> bool:
        # Step 6: check whether the required bits are set
        return (self.permissions & permission) == permission


if __name__ == "__main__":
    p = PatientPermissions()
    p.add_permission(p.READ | p.WRITE)
    print(p.has_permission(p.WRITE), p.permissions)
