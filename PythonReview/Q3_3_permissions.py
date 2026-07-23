"""Manage bitwise patient-data permissions."""
class PatientPermissions:
    READ=1; WRITE=2; DELETE=4; ALL=READ|WRITE|DELETE
    def __init__(self,permissions:int=0): self.permissions=permissions
    def add_permission(self,permission:int)->None: self.permissions|=permission
    def remove_permission(self,permission:int)->None: self.permissions&=~permission
    def has_permission(self,permission:int)->bool: return (self.permissions&permission)==permission
if __name__ == "__main__": p=PatientPermissions(); p.add_permission(p.READ|p.WRITE); print(p.has_permission(p.WRITE),p.permissions)
