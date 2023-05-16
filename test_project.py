from project import Bubble,Selection,Insertion,Linear,Binary

def test_Bubble():
    assert Bubble([4,99,2,43,10])==[2,4,10,43,99]
    assert Bubble([32,11,2,32,44])==[2,11,32,32,44]

def test_Insertion():
    assert Insertion([4,99,2,43,10])==[2,4,10,43,99]
    assert Insertion([32,11,2,32,44])==[2,11,32,32,44]

def test_Selection():
    assert Selection([4,99,2,43,10])==[2,4,10,43,99]
    assert Selection([32,11,2,32,44])==[2,11,32,32,44]

def test_Linear():
    assert Linear([1,2,3,4,5],5)==True
    assert Linear([1,2,3,4,5],2)==True
    assert Linear([1,2,3,4,5],3)==True
    assert Linear([1,2,3,4,5],7)==False
    assert Linear([1,2,3,6,7],4)==False

def test_Binary():
    assert Binary([1,2,3,4,5],5)==True
    assert Binary([1,2,3,4,5],2)==True
    assert Binary([1,2,3,4,5],3)==True
    assert Binary([1,2,3,4,5],7)==False
    assert Binary([1,2,3,6,7],4)==False