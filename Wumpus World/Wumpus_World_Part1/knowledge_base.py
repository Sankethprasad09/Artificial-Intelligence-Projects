# KnowledgeBase
# A knowledge base for a knowledge-based agent.
# SANKETH KARUTURI

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:
    """
    A KnowledgeBase that supports 'tell' (inserting information) and 'ask' (querying).
    For now, this is a stub implementation that always returns 'climb'.
    """

    def __init__(self):
        """
        Construct a new KnowledgeBase.
        """
        pass

    def tell(self, sentence):
        """
        Insert a sentence (knowledge) into the KB.
        For now, we do nothing.
        :param sentence: The knowledge to be inserted.
        """
        pass

    def ask(self, query):
        """
        Ask a query of the KB, returning an action in the wumpus world.
        For now, always return WumpusWorldAgent.climb as the default action.
        :param query: The query to be asked of the KB.
        :return: An action function from WumpusWorldAgent (e.g. WumpusWorldAgent.climb).
        """
        # Stub: Always return climb
        return WumpusWorldAgent.climb
