import input_
import import_
import export_


def start():
    if input_.mode() == '1':
        info = input_.exp()
        export_.export_func(info)

    else:
        info = input_.imp()
        import_.import_func(info)
