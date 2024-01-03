from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_given_todo_list_is_empty(context):
    context.todo_list = ToDoList()

@given('the to-do list contains tasks')
def step_given_todo_list_contains_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row["Task"])
        if "Status" in row and row["Status"] == "Completed":
            context.todo_list.mark_as_completed(row["Task"])

@when('the user adds task "{task}"')
def step_when_user_adds_task(context, task):
    context.todo_list.add_task(task)

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.listed_tasks = context.todo_list.list_tasks()

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_as_completed(context, task):
    context.todo_list.mark_as_completed(task)

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.todo_list.clear()

@when('the user adds tasks')
def step_when_user_adds_multiple_tasks(context):
    for row in context.table:
        context.todo_list.add_task(row["Task"])

@then('the to-do list should contain "{task}"')
def step_then_todo_list_contains_task(context, task):
    assert task in context.todo_list.list_tasks()

@then('the to-do list should show task "{task}" as completed')
def step_then_todo_list_show_completed(context, task):
    assert context.todo_list.is_task_completed(task)

@then('the to-do list should be empty')
def step_then_todo_list_empty(context):
    assert not context.todo_list.tasks

@then('the to-do list should contain tasks')
def step_then_todo_list_contains_tasks(context):
    expected_tasks = [row["Task"] for row in context.table]
    actual_tasks = context.todo_list.list_tasks()
    assert set(actual_tasks) == set(expected_tasks)


@when('the user adds a task "{task}"')
def step_when_user_adds_a_task(context, task):
    context.todo_list.add_task(task)

@then('the output should contain "{task}"')
def step_then_output_should_contain(context, task):
    assert task in context.todo_list.list_tasks()