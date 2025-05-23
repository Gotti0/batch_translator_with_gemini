# dtos.py
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Union
from pathlib import Path

# --- 모델 정보 DTO ---
@dataclass
class ModelInfoDTO:
    """
    사용 가능한 API 모델 정보를 전달하기 위한 DTO입니다.
    """
    name: str # 예: "models/gemini-2.0-flash"
    display_name: str # 예: "gemini-2.0-flash"
    description: Optional[str] = None
    version: Optional[str] = None
    input_token_limit: Optional[int] = None
    output_token_limit: Optional[int] = None

# --- 번역 작업 상태 DTO ---
@dataclass
class TranslationChunkStatusDTO:
    """
    개별 청크의 번역 상태를 나타내는 DTO입니다.
    """
    chunk_index: int
    status: str # 예: "PENDING", "PROCESSING", "COMPLETED", "FAILED"
    error_message: Optional[str] = None
    translated_content_preview: Optional[str] = None

@dataclass
class TranslationJobProgressDTO:
    """
    전체 번역 작업의 진행 상황을 나타내는 DTO입니다.
    """
    total_chunks: int
    processed_chunks: int
    successful_chunks: int
    failed_chunks: int
    current_status_message: str
    current_chunk_processing: Optional[int] = None # 수정: 필드 추가
    last_error_message: Optional[str] = None 


# --- 고유명사 추출 작업 상태 DTO ---
@dataclass
class PronounExtractionProgressDTO:
    """
    고유명사 추출 작업의 진행 상황을 나타내는 DTO입니다.
    """
    total_sample_chunks: int
    processed_sample_chunks: int
    current_status_message: str

# --- 설정 관련 DTO (필요시) ---
@dataclass
class AppConfigDisplayDTO:
    """
    UI에 표시하거나 전달하기 위한 간소화된 애플리케이션 설정 DTO입니다.
    (API 키와 같이 민감한 정보는 제외)
    """
    model_name: str
    temperature: float
    top_p: float
    chunk_size: int
    pronouns_csv_path: Optional[str] = None

# --- 사용자 입력 DTO (프레젠테이션 -> 애플리케이션) ---
@dataclass
class TranslationRequestDTO:
    """
    번역 시작 요청을 위한 DTO입니다.
    """
    input_file_path: Union[str, Path]
    output_file_path: Union[str, Path]

@dataclass
class PronounExtractionRequestDTO:
    """
    고유명사 추출 요청을 위한 DTO입니다.
    """
    input_file_path: Union[str, Path]


if __name__ == '__main__':
    # DTO 사용 예시
    print("--- DTO 사용 예시 ---")

    model1 = ModelInfoDTO(name="models/gemini-2.0-flash", display_name="gemini-2.0-flash", input_token_limit=1048576)
    print(f"모델 정보: {model1}")

    progress1 = TranslationJobProgressDTO(
        total_chunks=100,
        processed_chunks=25,
        successful_chunks=20,
        failed_chunks=5,
        current_status_message="청크 26/100 번역 중...",
        current_chunk_processing=25 # 추가된 필드 사용 예시
    )
    print(f"번역 진행: {progress1}")

    pronoun_progress = PronounExtractionProgressDTO(
        total_sample_chunks=50,
        processed_sample_chunks=10,
        current_status_message="표본 청크 11/50 분석 중..."
    )
    print(f"고유명사 추출 진행: {pronoun_progress}")

    config_display = AppConfigDisplayDTO(
        model_name="gemini-2.0-flash", 
        temperature=0.8,
        top_p=0.9,
        chunk_size=5000,
        pronouns_csv_path="data/my_pronouns.csv"
    )
    print(f"애플리케이션 설정 (표시용): {config_display}")

    trans_request = TranslationRequestDTO(
        input_file_path="input/source_text.txt",
        output_file_path="output/translated_text.txt"
    )
    print(f"번역 요청: {trans_request}")

