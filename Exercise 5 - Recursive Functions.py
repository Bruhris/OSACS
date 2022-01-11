def TowerOfHanoi(n , source, destination, extra):
    if n == 1:
        print("Move disk 1 from rod",source,"to rod",destination) # Move the shortest disk from current rod to destination
        return
    TowerOfHanoi(n-1, source, extra, destination) # Move all disks from rod A to rod C
    print("Move disk",n,"from rod",source,"to rod",destination) # Move biggest disk on bottom from rod A to rod C
    TowerOfHanoi(n-1, extra, destination, source) # Move all other disks in order of biggest to smallest from rod B to rod C while using rod A
         

n = int(input("Enter the number of disks "))
TowerOfHanoi(n, 'A', 'B', 'C')