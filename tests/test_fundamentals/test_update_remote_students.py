from fundamentals.update_remote_students import update_remote_students

def test_original_list_is_immutable():
    input = [{ "name": 'Euler', "age": 27 }]
    assert update_remote_students(input) == input

def test_update_remote_student():
    input = [{ "name": 'Euler', "age": 27 }]
    output = [{ "name": 'Euler', "age": 27, "location": 'remote' }]
    assert update_remote_students(input) == output
    
def test_update_remote_students():
    input =[{ "name": 'Hypatia', "age": 31, "location": 'leeds' },
            { "name": 'Ramanujan', "age": 22 },
            { "name": 'Tao', "age": 47, "location": 'manchester' }
        ]
    output=[{ "name": 'Hypatia', "age": 31, "location": 'leeds' },
            { "name": 'Ramanujan', "age": 22, "location": 'remote' },
            { "name": 'Tao', "age": 47, "location": 'manchester' }
        ]
    assert update_remote_students(input) == output