from concurrent import futures
import time
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

# 实现 proto 文件中定义的 GreeterServicer
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message = 'hello {msg}'.format(msg = request.name))

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='hello {msg}'.format(msg = request.name))

    def SayAddComdt(self, request, context):
        print("SayAddComdt11111111111")
        print(request.name)
        print(request.cate_id)
        print(request.price)
        code = 1024#len(request.name)
        if request.is_sale:
            curr_mess = "on buying"
        else:
            curr_mess = "不存在"
        return helloworld_pb2.AddComdtReply(code=len(request.name), mess=curr_mess.encode("utf-8"))

def serve():
    # 启动 rpc 服务8
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    print("start")
    serve()
    print("success")