from lmdeploy import pipeline, TurbomindEngineConfig, ChatTemplateConfig
import os

def load_pipeline(model_id="OpenGVLab/InternVL3-1B"):
    """
    初始化 InternVL3 模型並回傳推論用的 pipeline。
    """
    return pipeline(
        model_id,
        backend_config=TurbomindEngineConfig(session_len=16384, tp=1),
        chat_template_config=ChatTemplateConfig(model_name="internvl2_5")
    )
