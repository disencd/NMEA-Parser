from lib.common.inlet_factory import InletFactory


def run(args):
    inlet = InletFactory.create_executor(args.inlet)
    data = inlet.run()