@router.get("/{document_id}/analyze")
def analyze_document(document_id: str):

    result = DocumentService.analyze(document_id)

    return {
        "success": True,
        "message": "Document analyzed successfully",
        "data": result,
    }