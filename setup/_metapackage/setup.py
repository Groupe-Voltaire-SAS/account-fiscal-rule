import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-account-fiscal-rule",
    description="Meta package for oca-account-fiscal-rule Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_avatax',
        'odoo13-addon-account_avatax_sale',
        'odoo13-addon-account_fiscal_position_rule',
        'odoo13-addon-account_fiscal_position_rule_purchase',
        'odoo13-addon-account_fiscal_position_rule_sale',
        'odoo13-addon-account_multi_vat',
        'odoo13-addon-account_multi_vat_sale',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
