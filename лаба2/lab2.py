import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """
    Python provides its own interface of Prototype via `copy.copy` and
    `copy.deepcopy` functions. And any class that wants to implement custom
    implementations have to override `__copy__` and `__deepcopy__` member
    functions.
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Create a shallow copy. This method will be called whenever someone calls
        `copy.copy` with this object and the returned value is returned as the
        new shallow copy.
        """

        # спочатку створимо копії вкладених об’єктів
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # потім клонуємо сам об’єкт, використовуючи підготовлені клони вкладених об’єктів
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """
        Create a deep copy. This method will be called whenever someone calls
        `copy.deepcopy` with this object and the returned value is returned as
        the new deep copy.

        What is the use of the argument `memo`? Memo is the dictionary that is
        used by the `deepcopy` library to prevent infinite recursive copies in
        instances of circular references. Pass it to all the `deepcopy` calls
        you make in the `__deepcopy__` implementation to prevent infinite
        recursions.
        """
        if memo is None:
            memo = {}

        # спочатку створимо копії вкладених об’єктів
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # потім давайте клонуємо сам об’єкт, використовуючи підготовлені клони вкладених об’єктів
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    # давайте змінимо список у shallow_copied_component і подивимося, чи зміниться він у компоненті
    shallow_copied_component.some_list_of_objects.append("another object")
    if component.some_list_of_objects[-1] == "another object":
        print(
            "додавання елементів до `shallow_copied_component` "
            "some_list_of_objects додає його до `component` "
            "some_list_of_objects."
        )
    else:
        print(
            "додавання елементів до `shallow_copied_component` "
            "some_list_of_objects не додає його до `component` "
            "some_list_of_objects."
        )

    # змінимо набір у списку об'єктів
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "зміна об'єктів у some_list_of_objects компонента "
            "змінює цей об'єкт у `shallow_copied_component` "
            "some_list_of_objects."
        )
    else:
        print(
            "зміна об'єктів у some_list_of_objects компонента "
            "змінює цей об'єкт у`shallow_copied_component` "
            "some_list_of_objects."
        )

    deep_copied_component = copy.deepcopy(component)

    # змінимо список у deep_copied_component і подивимося, чи зміниться він у компоненті
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print(
            "додавання елементів до `deep_copied_component` "
            "some_list_of_objects додає його до `component` "
            "some_list_of_objects."
        )
    else:
        print(
            "додавання елементів до `deep_copied_component` "
            "some_list_of_objects doesn't додає його до `component` "
            "some_list_of_objects."
        )

    # змінимо набір у списку об'єктів
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "зміна об'єктів в `component` some_list_of_objects "
            "змінює цей об’єкт `deep_copied_component` "
            "some_list_of_objects."
        )
    else:
        print(
            "зміна об'єктів в `component` some_list_of_objects "
            "змінює цей об’єкт `deep_copied_component` "
            "some_list_of_objects."
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ Це показує, що глибоко скопійовані об’єкти містять однакове посилання, вони не клонуються повторно "
        )