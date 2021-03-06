# fork полностью дублирует родительский процесс
import time
import os

pid = os.fork()

if pid == 0:
    # дочерний процесс
    while True:
        print("child: ", os.getpid())
        time.sleep(5)
else:
    # родительский процесс
    print("parent: ", os.getpid())
    # с помощью этой команды мы ждём пока выполнится дочерний процесс
    os.wait()

# для отображения процесса в древовидном формате можно использовать такую команду
#
