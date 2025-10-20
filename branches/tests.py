from django.test import TestCase
from graphene.test import Client
from .schema import schema
from .models import Bank, Branch

class GraphQLTestCase(TestCase):
    """
    Test case for GraphQL queries.
    """

    def setUp(self):
        # Create sample banks
        bank1 = Bank.objects.create(name="State Bank of India")
        bank2 = Bank.objects.create(name="HDFC Bank")

        # Create sample branches
        Branch.objects.create(branch="Sion Branch", ifsc="SBIN0001234", bank=bank1)
        Branch.objects.create(branch="Andheri Branch", ifsc="HDFC0005678", bank=bank2)

        # Initialize GraphQL client
        self.client = Client(schema)

    def test_branches_query(self):
        """
        Test the branches GraphQL query.
        """
        query = '''
        query {
            branches {
                edges {
                    node {
                        branch
                        ifsc
                        bank {
                            name
                        }
                    }
                }
            }
        }
        '''
        executed = self.client.execute(query)

        # Check the response contains 'branches'
        self.assertIn("branches", executed["data"])

        # Check there are exactly 2 branches
        self.assertEqual(len(executed["data"]["branches"]["edges"]), 2)

        # Check branch names
        self.assertEqual(
            executed["data"]["branches"]["edges"][0]["node"]["branch"], "Sion Branch"
        )
        self.assertEqual(
            executed["data"]["branches"]["edges"][1]["node"]["branch"], "Andheri Branch"
        )
