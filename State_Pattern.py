# coding:utf-8

# 有25分钱状态
class HasQuarterState(object):
    def __init__(self, gumballMachine):  # 传入糖果机的实例
        self.gumballMachine = gumballMachine

    def insertQuarter(self):  # 投入25分钱动作
        print("You cannot insert another quarter")

    def ejectQuarter(self):  # 退出25分钱动作
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())  # 之后糖果机的状
        # 态切换到没有25分钱状态

    def turnCrank(self):  # 转动曲柄动作
        print("You turned....")
        self.gumballMachine.setState(self.gumballMachine.getSoldState())  # 之后糖果机的状
        # 态切换到售出糖果状态

    def dispense(self):  # 发放糖果动作，这是个内部动作，此处实现没有作用
        print("No gumball dispense")


# 糖果售罄状态
class SoldOutState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        print("You turned, but there's no gumball")

    def dispense(self):
        print("No gumball dispense")


# 没有25分钱状态
class NoQuarterState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")


# 售出糖果状态
class SoldState(object):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


# 糖果机类
class GumballMachine:
    def __init__(self, numberGumballs):
        self.count = numberGumballs
        # =========创建每一个状态的状态实例====================#
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        # =========end=========================================#
        if self.count > 0:
            self.state = self.noQuarterState

    # ============每个状态的get方法和set方法===============#

    def getSoldOutState(self):
        return self.soldOutState

    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldState(self):
        return self.soldState

    def setState(self, state):
        self.state = state

    # =========end=========================================#

    # ============将方法委托给当前的状态===================#

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        if self.state == self.hasQuarterState:
            self.state.turnCrank()
            self.state.dispense()
        else:
            self.state.turnCrank()

    # =========end=========================================#

    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1

    # ============检查状态和糖果数量的方法=================#

    def getState(self):
        print('The State is: ' + type(self.state).__name__)
        return self.state

    def getCount(self):
        print('The Count is: ' + str(self.count))
        return self.count


def main():
    gumballMachine = GumballMachine(2)
    gumballMachine.getCount()
    gumballMachine.getState()
    print("=====================================================")
    gumballMachine.insertQuarter()
    gumballMachine.getState()
    gumballMachine.ejectQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.getState()
    gumballMachine.turnCrank()
    gumballMachine.getState()
    gumballMachine.getCount()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.getState()
    print("=====================================================")
    gumballMachine.turnCrank()


if __name__ == '__main__':
    main()

'''
状态机
'''

from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition


@acts_as_state_machine
class Process:
    # 定义状态
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()
    # 定义事件
    wait = Event(from_states=(created, running, blocked, swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked), to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    @after('wait')
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate')
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print('Error: transition of {} from {} to {} failed'.format(process.name, process.current_state, event_name))


def state_info(process):
    print('state of {}: {}'.format(process.name, process.current_state))


def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'
    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]
    print()

    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]
    print()

    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]
    print()

    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]
    print()

    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]
    print()

    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]


if __name__ == '__main__':
    main()
