# 验证 langchain-openai 安装
import sys
import subprocess

def verify_installation():
    """验证 langchain-openai 是否正确安装"""
    try:
        # 检查是否安装了 langchain-openai
        result = subprocess.run([
            sys.executable, "-c", 
            "import langchain_openai; print('langchain-openai 可用')"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ langchain-openai 安装成功！")
            print(result.stdout)
            return True
        else:
            print("❌ langchain-openai 未正确安装")
            print("错误:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 验证失败: {e}")
        return False

if __name__ == "__main__":
    print("Python 路径:", sys.executable)
    verify_installation()