from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    job_types = []
    for type in jobs:
        if (type["job_type"] in job_types):
            job_types = job_types
        else:
            job_types.append(type["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    job_types = []
    for type in jobs:
        if (type["job_type"] == job_type):
            job_types.append(type)
        else:
            job_types = job_types
    return job_types


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs = read(path)
    job_industries = []
    for industry in jobs:
        if (industry["industry"] in job_industries):
            job_industries = job_industries
        elif (industry["industry"] == ""):
            job_industries = job_industries
        else:
            job_industries.append(industry["industry"])
    return job_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    industry_filter = []
    for industries in jobs:
        if (industries["industry"] == industry):
            industry_filter.append(industries)
        else:
            industry_filter = industry_filter
    return industry_filter


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    max_salary = 0
    for salary in jobs:
        if (salary["max_salary"].isnumeric()):
            if (int(salary["max_salary"]) > int(max_salary)):
                max_salary = salary["max_salary"]
            else:
                max_salary = max_salary
        else:
            max_salary = max_salary
    return int(max_salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    min_salary = get_max_salary(path)
    for salary in jobs:
        if (salary["min_salary"].isnumeric() and
                int(salary["min_salary"]) < int(min_salary)):
            min_salary = salary["min_salary"]
        else:
            min_salary = min_salary
    return int(min_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if ("min_salary" not in job or "max_salary" not in job or
            type(job["min_salary"]) != int or
            type(job["max_salary"]) != int or
            job["max_salary"] < job["min_salary"] or
            type(salary) != int):
        raise ValueError
    else:
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    salary_filter = []
    for salaries in jobs:
        try:
            if matches_salary_range(salaries, salary):
                salary_filter.append(salaries)
            else:
                salary_filter = salary_filter
        except ValueError:
            salary_filter = salary_filter
    return salary_filter
