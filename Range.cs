using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace AlgorithmTools
{
    public class Range : IEnumerable<int>
    {
        private int delta;
        
        // Fields of range: [From; To).
        public int From { get; set; }
        public int To { get; set; }

        // Delta is the counting offset. It denotes difference between two nearby elements.
        public int Delta
        {
            get => delta;

            set
            {
                if (value == 0)
                    throw new ArgumentException("Delta must be non-zero.");

                delta = value;
            }
        }

        // Current value of counter; it is set to from value before counting.
        public int Current { get; set; }
        
        public Range(int to)
        {
            To = to;
            Current = From = 0;
            Delta = 1;
        }

        public Range(int from, int to, int delta = 1)
        {
            To = to;
            Current = From = from;
            Delta = delta;
        }

        // Counting.
        public IEnumerator<int> GetEnumerator()
        {
            for (Current = From; Current < To; Current += Delta)
                yield return Current;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        // Parallel counting.
        public ParallelLoopResult ParallelLoop(Action<int> method) => Parallel.ForEach(this, method);
        public ParallelLoopResult ParallelLoop(Action<int, ParallelLoopState> method) => Parallel.ForEach(this, method);
    }
}
