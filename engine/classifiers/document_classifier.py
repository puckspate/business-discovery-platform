from engine.knowledge.document_types import DOCUMENT_TYPES


class DocumentClassifier:

    @staticmethod
    def classify(headers):

        normalized = {
            str(h).strip().lower()
            for h in headers
            if h
        }

        best_match = None
        best_score = 0

        for document_type, config in DOCUMENT_TYPES.items():

            keywords = set(config["keywords"])

            matches = normalized.intersection(keywords)

            score = len(matches)

            if score > best_score:
                best_score = score
                best_match = document_type

        confidence = 0

        if best_match:
            confidence = round(
                best_score /
                len(DOCUMENT_TYPES[best_match]["keywords"]),
                2,
            )

        return {
            "document_type": best_match or "Unknown",
            "confidence": confidence,
        }