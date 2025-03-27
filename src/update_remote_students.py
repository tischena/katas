# The challenge is to implement a function that updates missing
# location info for students attending Northcoders.

# This function will be called with a list of dictionaries. 
# Each dictionary represents a student on a Northcoders 
# bootcamp. Some of the students have a specified location
# property which is a string of the office they will be 
# attending during their time on the course. For some students,
# that property is missing.

# Your function should return a new list, where all 
# dictionaries that were missing a location have been updated
# so that they now have a location property with a value of 
# "remote". All other properties should remain as they were.

# This function must be a pure function, i.e. it should have
# no side effects. Your test suite should reflect this.

# Examples
# update_remote_students([{ "name": 'Euler', "age": 27 }])

# #  should return
# [{ "name": 'Euler', "age": 27, "location": 'remote' }]
# All dictionaries with existing "location"s should 
# remain unchanged.

# update_remote_students([
#   { "name": 'Hypatia', "age": 31, "location": 'leeds' },
#   { "name": 'Ramanujan', "age": 22 },
#   { "name": 'Tao', "age": 47, "location": 'manchester' }
# ])

# # should return
# [
#   { "name": 'Hypatia', "age": 31, "location": 'leeds' },
#   { "name": 'Ramanujan', "age": 22, "location": 'remote' },
#   { "name": 'Tao', "age": 47, "location": 'manchester' }
# ]

def update_remote_students(students_list):
    updated_list = []
    for student_dict in students_list:
        if 'location' in student_dict.keys():
            updated_list.append(student_dict)
        else:
            student_dict['location'] = 'remote'
            updated_list.append(student_dict)
    return updated_list