  #!/usr/bin/pythbbbon3
 def new_in_list(my_list, idx, element):
    l = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        l[idx] = element
        return l
