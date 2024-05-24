def before_all(context):
    print("Before all")
    context.browser = "Chrome"
    # context.browser = "Firefox"
    # context.browser = "Opera"


def before_feature(context, feature):
    print("Before feature")


def before_scenario(context, scenario):
    print("Before scenario")


def before_step(context, step):
    print("Before step")


def after_step(context, step):
    print("After step")


def after_scenario(context, scenario):
    print("After scenario")
    context.driver.quit()


def after_feature(context, feature):
    print("After feature")


def after_all(context):
    print("After all")

