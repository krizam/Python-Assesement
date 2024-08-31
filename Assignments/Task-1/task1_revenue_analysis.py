import os
import glob

def process_department_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:] 
    
    total_q1, total_q2, total_q3, total_q4 = 0, 0, 0, 0
    employee_count = 0
    failed_count = 0
    
    for line in lines:
        q1, q2, q3, q4, emp_id = line.strip().split()
        q1, q2, q3, q4 = map(float, (q1, q2, q3, q4))
        
        total_q1 += q1
        total_q2 += q2
        total_q3 += q3
        total_q4 += q4
        employee_count += 1
        
        if q1 + q2 + q3 + q4 < 80000:
            failed_count += 1
    
    avg_q1 = total_q1 / employee_count
    avg_q2 = total_q2 / employee_count
    avg_q3 = total_q3 / employee_count
    avg_q4 = total_q4 / employee_count
    
    return avg_q1, avg_q2, avg_q3, avg_q4, failed_count

def main():
    for file_path in glob.glob('Task-1/*.txt'):
        if file_path.endswith('_avg.txt') or file_path.endswith('_failed.txt'):
            continue
        
        dept_code = os.path.splitext(file_path)[0]
        avg_q1, avg_q2, avg_q3, avg_q4, failed_count = process_department_file(file_path)
        
        with open(f'{dept_code}_avg.txt', 'w') as avg_file:
            avg_file.write(f'Quarter 1 Average: {avg_q1:.2f}\n')
            avg_file.write(f'Quarter 2 Average: {avg_q2:.2f}\n')
            avg_file.write(f'Quarter 3 Average: {avg_q3:.2f}\n')
            avg_file.write(f'Quarter 4 Average: {avg_q4:.2f}\n')
        
        with open(f'{dept_code}_failed.txt', 'w') as failed_file:
            failed_file.write(f'Number of employees who did not meet the annual revenue target: {failed_count}\n')

if __name__ == '__main__':
    main()