import argparse


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION]",
        description="Deploy all SQL table und function files to database and run tests.",
    )
    
    parser.add_argument(
        "--check-database-version-difference",
        metavar="check_database_version_difference",
        default=False,
        help="redeploy database if different",
    )

    parser.add_argument(
        "--delete-redeploy-if-version-different",
        metavar="delete_redeploy_if_version_different",
        default=False,
        help="delete and redeploy database if different",
    )
    
if __name__=="__main__":
    parser = init_argparse()
    args = parser.parse_args()
    
    print(f"args.check_database_version_difference : {args.check_database_version_difference}")
    print(f"type - args.check_database_version_difference : {type(args.check_database_version_difference)}")
    print(f"args.delete_redeploy_if_version_different : {args.delete_redeploy_if_version_different}")
    print(f"type - args.delete_redeploy_if_version_different : {type(args.delete_redeploy_if_version_different)}")